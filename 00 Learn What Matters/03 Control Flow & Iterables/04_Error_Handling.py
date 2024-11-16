# Using try, except, else, and finally
try:
    # Raise an exception
    raise IndexError("This is an index error")
except IndexError as e:
    print("Caught an IndexError:", e)
except (TypeError, NameError):
    print("Caught a TypeError or NameError")
else:
    print("No exceptions occurred")
finally:
    print("This block always runs for cleanup")
