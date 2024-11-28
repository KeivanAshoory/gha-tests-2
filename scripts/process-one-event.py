import json
import sys
import random
import time


def main(action_str, event_str):
    print(f'action is: {action_str}')
    print(f'event is: {event_str}')

    event = json.loads(event_str)
    if 'event_type' not in event:
        print('Invalid event!')
        sys.exit(2)

    delay = random.randint(2, 10)
    success = random.randint(0, 4)

    print(f'sleep for {delay}')
    time.sleep(delay)
    if success == 0:
        print('Failed to completed the process')
        sys.exit(1)
    else:
        print('Succeeded to completed the process')
        sys.exit(0)


if __name__ == '__main__':
    in_action = sys.argv[1]
    in_event = sys.argv[2]
    main(in_action, in_event)
