"""Scheduling work on a jobsite is one of the most difficult tasks in
construction management. Different contractors work on different
trades and can only do so much work in a single day. We need to
make sure that we have the right people on the job site every day
and anticipate how many days it will take to complete a set of tasks.

Requirements:
    Your solution should prefer to finish the work as fast as possible

"""
import unittest

WORKERS = [
    {
        'email': 'bob@brickwork.com',
        'trades': ['brickwork'],
        'cost': 90,
    },
    {
        'email': 'alice@example.com',
        'trades': ['brickwork', 'drywall'],
        'cost': 100,
    },
    {
        'email': 'charlie@cement.com',
        'trades': ['cement'],
        'cost': 80,
    },
    {
        'email': 'wally@walls.com',
        'trades': ['cement', 'drywall'],
        'cost': 95,
    },
]


class WorkScheduler:
    def __init__(self, workers):
        self.workers = workers

    def suitable_workers(self, trade):
        """Given a suitable trade, returns a list of emails of workers who
        work the specified trade

        Args:
            trade (str): specific trade desired 'brickwork', 'drywall', or 'cement'

        Returns:
            List of worker's emails sorted alphabetically - ['email1',
            'email2', 'etc...']

        """
        emails = []
        for worker in self.workers:
            if trade in worker["trades"]:
                emails.append(worker["email"])

        return sorted(emails)

    def schedule_one_day(self, trades):
        """Given a list of trades, return a list of worker emails that can work
        that day.  A worker cannot work multiple trades in one day, and if
        there are multiple workers available to work on a particular trade, the
        worker with the cheapest cost should be chosen.

        Args:
            trades list(str): a list of trades. Each trade represents 1
            unit of work that needs to be completed

        Returns:
            List of worker emails that are scheduled for the day, in the order that they
            were scheduled (i.e. in the same order that the trades were provided).

        """

        schedule_workers = []
        used_workers = set()
        for trade in trades:
            avialable_workers = [worker for worker in self.workers if
                                 trade in worker["trades"] and worker["email"] not in used_workers]

            if len(avialable_workers) > 0:
                best_worker = min(avialable_workers, key=lambda w: w["cost"])

                schedule_workers.append(best_worker["email"])
                used_workers.add(best_worker["email"])
        return schedule_workers

    def schedule_all_tasks(self, trades):
        """Given a list of trades, schedules work for each day, until all the
        trades are scheduled. A worker cannot work multiple trades in one day,
        and if there are multiple workers available to work on a particular
        trade, the worker with the cheapest cost should be chosen.


        Args:
            trades list(str): a list of trades. Each trade represents 1
            unit of work

        Returns:
            list(list(string)): List of scheduled days.  Each day is a list
            of worker emails for work scheduled for that day.
            Example Input: ['brickwork', 'brickwork', 'brickwork']
            Example Output:  [['bob@brickwork.com', 'alice@example.com'],
            ['bob@brickwork.com']]

        """
        all_scheduled_days = []
        while trades:
            scheduled_for_day = self.schedule_one_day(trades)
            if not scheduled_for_day:
                break
            all_scheduled_days.append(scheduled_for_day)
            trades = trades[len(scheduled_for_day):]
        return all_scheduled_days


class TestWorkScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = WorkScheduler(WORKERS)

    def test_can_find_a_suitable_worker_for_a_task(self):
        self.assertListEqual(self.scheduler.suitable_workers('cement'),
                             ['charlie@cement.com', 'wally@walls.com'])
        self.assertListEqual(self.scheduler.suitable_workers('brickwork'),
                             ['alice@example.com', 'bob@brickwork.com'])
        self.assertListEqual(self.scheduler.suitable_workers('drywall'),
                             ['alice@example.com', 'wally@walls.com'])

    def test_can_build_a_simple_schedule_for_one_day(self):
        self.assertListEqual(self.scheduler.schedule_one_day(['cement']),
                             ['charlie@cement.com'])
        self.assertListEqual(self.scheduler.schedule_one_day(['brickwork']),
                             ['bob@brickwork.com'])
        self.assertListEqual(self.scheduler.schedule_one_day(['drywall']),
                             ['wally@walls.com'])
        self.assertListEqual(self.scheduler.schedule_one_day(
            ['cement', 'drywall']), ['charlie@cement.com',
                                     'wally@walls.com'])
        self.assertListEqual(self.scheduler.schedule_one_day(
            ['cement', 'brickwork']), ['charlie@cement.com',
                                       'bob@brickwork.com'])
        self.assertListEqual(self.scheduler.schedule_one_day(
            ['drywall', 'brickwork']), ['wally@walls.com',
                                        'bob@brickwork.com'])
        self.assertListEqual(self.scheduler.schedule_one_day(
            ['cement', 'brickwork', 'drywall']), ['charlie@cement.com',
                                                  'bob@brickwork.com',
                                                  'wally@walls.com'])

    def test_does_not_double_book_workers(self):
        self.assertListEqual(self.scheduler.schedule_one_day(
            ['cement', 'cement', 'cement']), ['charlie@cement.com',
                                              'wally@walls.com'])
        self.assertListEqual(self.scheduler.schedule_one_day(
            ['brickwork', 'brickwork', 'brickwork']), ['bob@brickwork.com',
                                                       'alice@example.com'])
        self.assertListEqual(self.scheduler.schedule_one_day(
            ['drywall', 'drywall', 'drywall']), ['wally@walls.com',
                                                 'alice@example.com'])

    def test_can_schedule_multiple_days_of_work(self):
        schedule1 = self.scheduler.schedule_all_tasks(
            ['brickwork', 'brickwork', 'brickwork'])
        self.assertTrue('bob@brickwork.com' in schedule1[0])
        self.assertTrue('alice@example.com' in schedule1[0])
        self.assertTrue('bob@brickwork.com' in schedule1[1])

        schedule2 = self.scheduler.schedule_all_tasks(
            ['drywall', 'drywall', 'drywall'])
        self.assertTrue('wally@walls.com' in schedule2[0])
        self.assertTrue('alice@example.com' in schedule2[0])
        self.assertTrue('wally@walls.com' in schedule2[1])

        schedule3 = self.scheduler.schedule_all_tasks(
            ['cement', 'cement', 'cement'])
        self.assertTrue('charlie@cement.com' in schedule3[0])
        self.assertTrue('wally@walls.com' in schedule3[0])
        self.assertTrue('charlie@cement.com' in schedule3[1])

    def test_can_schedule_all_work_optimistically(self):
        schedule1 = self.scheduler.schedule_all_tasks(
            ['cement', 'cement', 'cement', 'brickwork'])
        self.assertTrue('charlie@cement.com' in schedule1[0])
        self.assertTrue('bob@brickwork.com' in schedule1[0])
        self.assertTrue('wally@walls.com' in schedule1[0])
        self.assertTrue('charlie@cement.com' in schedule1[1])

        schedule2 = self.scheduler.schedule_all_tasks(
            ['cement', 'cement', 'drywall', 'drywall', 'cement',
             'brickwork'])
        self.assertTrue('charlie@cement.com' in schedule2[0])
        self.assertTrue('bob@brickwork.com' in schedule2[0])
        self.assertTrue('alice@example.com' in schedule2[0])
        self.assertTrue('wally@walls.com' in schedule2[0])
        self.assertTrue('charlie@cement.com' in schedule2[1])
        self.assertTrue('wally@walls.com' in schedule2[1])

        schedule3 = self.scheduler.schedule_all_tasks(
            ['cement', 'cement', 'brickwork', 'brickwork', 'cement',
             'brickwork'])
        self.assertTrue('charlie@cement.com' in schedule3[0])
        self.assertTrue('bob@brickwork.com' in schedule3[0])
        self.assertTrue('alice@example.com' in schedule3[0])
        self.assertTrue('wally@walls.com' in schedule3[0])
        self.assertTrue('charlie@cement.com' in schedule3[1])
        self.assertTrue('bob@brickwork.com' in schedule3[1])


unittest.main(exit=False)
