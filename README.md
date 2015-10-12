# python-timer
a wrapper for long-running tasks that iterate over many things, printing friendly 'percentage done' messages to standard error.


    import timer
    for stuff in timer.show_progress(range(100)):
        # .... analysis here
        timer.sleep(.5)

prints (to standard error) :

        : 0.1 min elapsed, 25.0 % done, ETA:   0.3 min
        : 0.1 min elapsed, 45.0 % done, ETA:   0.3 min
        : 0.2 min elapsed, 65.0 % done, ETA:   0.3 min
        : 0.3 min elapsed, 85.0 % done, ETA:   0.3 min
