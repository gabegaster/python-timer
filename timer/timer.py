'''
# Gabe Gaster, 2013
#
#   about every minute, eta will report how many iterations
#   have been performed and the Expected Time to Completion (the E.T.C.)
#
#####################################################################
#
# Examples:
#

import timer

for stuff in timer.show_progress(range(100)):
    # .... analysis here
    timer.sleep(.5)

# prints (to standard error) :
  # 0.1 min elapsed, 25.0 % done, ETA:   0.3 min
  # 0.1 min elapsed, 45.0 % done, ETA:   0.3 min
  # 0.2 min elapsed, 65.0 % done, ETA:   0.3 min
  # 0.3 min elapsed, 85.0 % done, ETA:   0.3 min

'''

import time
import sys

def get_time_str(num_secs):
    minutes = num_secs * 1. / 60
    hours = minutes / 60
    days = hours / 24
    if num_secs < 60:
        if num_secs < .001:
            return "%5.3f microsec" % num_secs*10**6
        elif .001 < num_secs < 1:
            return "%5.3f millisec" % num_secs*10**3
        else:
            return "%5.1f sec" % num_secs
    if minutes < 60:
        return "%5.1f min" % minutes
    elif hours < 24:
        return "%5.1f hours" % hours
    else:
        return "%5.1f days" % days


def show_progress(iterable, update_time=60, length=None):
    """Wraps any iterable and passes values right through. Every
    update_time's worth of seconds (defaulting to 60 seconds), print a
    report on total time elapsed, percent done and estimated total
    time of completion.

    If length is not specified, look to the length of iterable (if
    it's defined in __len__).

    If there is no length, then report number (instead of percent)
    done, and report time per iteration (instead of ETA).

    """
    name, length = get_name_length(iterable, length)

    start = last_update = time.time()
    # if the length is unknown, don't estimate completion time, but
    # still show periodic progress updates.

    for count, thing in enumerate(iterable):
        now = time.time()
        if now - last_update > update_time:
            last_update = now
            msg = get_msg(count, length, now, start)
            print >> sys.stderr, "%s : %s" % (name, msg)
        yield thing

    time_string = get_time_str(time.time() - start)
    print >> sys.stderr, "%s : DONE in %s" % (name, time_string)


def get_name_length(iterable, length):
    try:
        name = iterable.__name__
    except AttributeError:
        name = ""  # iterable.__repr__()
    if not hasattr(iterable, "__iter__"):
        raise TypeError("Object %s not iterable" % name)
    if hasattr(iterable, "__len__") and length is None:
        length = iterable.__len__()
    return name, length


def get_msg(count, length, now, start):
    time_elapsed = now - start
    if length:
        percent_done = 1. * count / length
        if percent_done:
            etc_secs = time_elapsed / percent_done
            etc_time = get_time_str(etc_secs)
        else:
            etc_time = "NA"
        msg = "%s elapsed, %5.3f%% done, ETC: %s"
        msg = msg % (get_time_str(time_elapsed),
                     percent_done * 100,
                     etc_time)
    else:
        msg = "%s elapsed, %s done : %s per iter"
        msg = msg % (get_time_str(time_elapsed),
                     count,
                     get_time_str(time_elapsed / count))
    return msg


def test():
    import StringIO

    sys.stderr = StringIO.StringIO()
    for j in show_progress(xrange(30),
                           update_time=1,
                           length=30):
        time.sleep(.1)
    msgs = sys.stderr.getvalue().split("\n")
    msgs = [i for i in msgs if i]
    assert len(msgs) == 3

if __name__ == "__main__":
    test()
