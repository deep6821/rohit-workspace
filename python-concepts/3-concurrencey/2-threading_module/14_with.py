"""
With:
-----
- Programs often use resources other than CPU time, including access to local
  disks, network sockets, and databases etc.
- The usage pattern is usually a try-except-finally block. Any cleanup actions
  are performed in the finally block. An alternative to the usual boilterplate
  code is to use the with statement. The with statement wraps the execution of
  a block of statements in a context defined by a context manager object.

Context Management Protocol:
----------------------------
- A context manager object abides by the context management protocol, which
  states that an object defines the following two methods.

- Python calls these two methods at appropriate times in the resource
  management cycle:

1. __enter__()
2. __exit__()

"""