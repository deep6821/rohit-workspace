import pandas as pd
import pprint
from datetime import datetime
from pyspark.sql.functions import col, count, from_unixtime, percentile_approx


COL_NAME_MAP = {
    "overall": "overall",
    "verified": "verified",
    "reviewTime": "review_time",
    "reviewerID": "reviewer_id",
    "asin": "asin",
    "reviewerName": "reviewer_name",
    "reviewText": "review_text",
    "summary": "summary",
    "unixReviewTime": "unix_review_time",
    "style": "style",
    "vote": "vote"
}

SELECTED_COLUMNS = [
    "reviewer_id",
    "asin",
    "review_text",
    "summary",
    "verified",
    "overall",
    "vote",
    "unix_review_time",
    "review_time",
]

def rename_columns(df, col_name_map, data_library='pandas'):
    if data_library == 'pandas':
        return df.rename(columns=col_name_map)
    
    elif data_library == 'pyspark':
        for old_name, new_name in col_name_map.items():
            df = df.withColumnRenamed(old_name, new_name)
    return df

def select_columns(df, columns, data_library='pandas'):
    if data_library == 'pandas':
        return df[columns]
    
    elif data_library == 'pyspark':
        return df.select(columns)

def repartitioning_and_saving(df,PATH_SNAPSHOT):
    """Repartitioning and saving the snapshot"""
    df = df.repartition('reviewed_year', 'reviewed_month').sortWithinPartitions("asin")
    df.write.mode("overwrite").parquet(PATH_SNAPSHOT)

def add_timestamp_column(df, data_library='pandas'):
    if data_library == 'pandas':
        df['reviewed_at'] = df[['unix_review_time']].applymap(datetime.fromtimestamp)
    
    elif data_library == 'pyspark':
        df = df.withColumn('reviewed_at', from_unixtime(col('unix_review_time')))

    return df

def fill_na_with_value(df, data_library='pandas'):
    if data_library == 'pandas':
        df['vote'] = df['vote'].fillna(value=0)
    
    elif data_library == 'pyspark':
        df = df.fillna({'vote': 0})
    
    return df

def average_review(df, data_library="pandas"):
    if data_library == 'pandas':
        unique_asin = len(df['asin'].unique())
        total_review = len(df)
        avg_review = total_review / unique_asin 
        return avg_review
    
    elif data_library == 'pyspark':
        unique_asin = df.select('asin').distinct().count()
        total_review = df.count()
        avg_review = total_review / unique_asin
        return avg_review
    
def count_reviews_by_product(df, asin, data_library='pandas'):
    if data_library == 'pandas':
        review_by_product = df.groupby('asin')['asin'].count()
        return review_by_product
    
    elif data_library == 'pyspark':
        review_by_product = df.groupBy('asin').count()
        return review_by_product

def show_review_text_stat(df, data_library='pandas'):
    if data_library == 'pandas':
        stat = df['review_text_len'].describe().to_dict() 
        weird_reviews = len(df[df['review_text_len'] <= 1])
        print("Review Length Stat")
        pprint(stat)
        print(f"Reviews with length one or less: {weird_reviews}")
    elif data_library == 'pyspark':
        summary_df = df.select('review_text_len').summary("count", "min", "25%", "75%", "max")
        summary = summary_df.rdd.map(lambda row: row.asDict(recursive=True)).collect()
        print("Review Length Stat")
        pprint(summary)
        weird_reviews = df.filter(col('review_text_len') <= 1).count()
        print(f"Reviews with length one or less: {weird_reviews}")

def calculate_median_review_count_by_year(main_df, data_library='pandas'):
    """
    Calculates the median review count by year for all products and top-rated products.

    Args:
        main_df (DataFrame): Input DataFrame containing review data.

    Returns:
        DataFrame: DataFrame with median review counts by year for all products and top-rated products.
    """
    if data_library == "pandas":
        main_df['review_year'] = main_df['reviewed_at'].dt.year 
        main_df['review_month'] = main_df['reviewed_at'].dt.month
        median_review_by_year_df = (
            main_df
            .groupby(['asin', 'review_year']) 
            .agg(median_review=("asin", "count")) 
            .reset_index()
            .groupby('review_year') 
            .agg({'median_review': 'median'})
            .reset_index()
        )

        # Find median yearly review of the top products
        review_top_item_by_year = ( 
            main_df[main_df['overall'] > 4]
            .groupby(['asin', 'review_year']) 
            .agg(median_review=("asin", "count")) 
            .reset_index() .groupby('review_year') 
            .agg({'median_review': 'median'}) 
            .reset_index()
        )
        print('Median Review by Year ',median_review_by_year_df)
        print('Review of top item by Year ',review_top_item_by_year)
        print('Code Executed Successfully')
        
    elif data_library == 'pyspark':
        median_review_by_year_df = (
            main_df
            .groupby('asin', 'reviewed_year') 
            .agg(count('asin')
            .alias('count')) 
            .groupby('reviewed_year') 
            .agg(percentile_approx('count', 0.5)
            .alias('median')) 
            .orderBy('reviewed_year', ascending=True)
        )   

        review_top_item_by_year = ( 
            main_df
            .filter(col('overall') > 4) 
            .groupby('asin', 'reviewed_year') 
            .agg(count('asin')
            .alias('count'))
            .groupby('reviewed_year') 
            .agg(percentile_approx('count', 0.5)
            .alias('median'))
            .orderBy('reviewed_year', ascending=True) 
        )
        
        return median_review_by_year_df, review_top_item_by_year
