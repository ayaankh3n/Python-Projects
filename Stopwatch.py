import time

def stopwatch(): 
    print("Press ENTER to start the stopwatch. Press Ctrl + C to stop.")
    input()
    start_time = time.time()
    try: 
        while True:
            elapsed_time = time.time() - start_time
            print("Elapsed Time: {elapsed_time:.2f} seconds", end = "\r")
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopwatch stopped!")
    
stopwatch()

