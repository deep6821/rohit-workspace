"""
Pool Executors:
---------------
In the previous sections, we studied how to create and manage threads and processes. However, managing these entities can be taxing on the developer so Python alleviates this burden by providing an interface which abstracts away the subtleties of starting and tearing down threads or processes. The concurrent.futures package provides the Executor interface which can be used to submit tasks to either threads or processes. The two subclasses are:

ThreadPoolExecutor

ProcessPoolExecutor

Tasks can be submitted synchronously or asynchronously to the pools for execution.
"""