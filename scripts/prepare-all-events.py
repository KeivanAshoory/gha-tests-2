import json


def main():
    events = [
        {'event_type': 'EVENT_TYPE_1', 'event_data': 'EVENT_DATAAAAA'},
        {'event_type': 'EVENT_TYPE_2', 'event_data': 'EVENT_DATAAAAA'},
        {'event_type': 'EVENT_TYPE_3', 'event_data': 'EVENT_DATAAAAA'},
        {'event_type': 'EVENT_TYPE_4', 'event_data': 'EVENT_DATAAAAA'},
        {'event_type': 'EVENT_TYPE_5', 'event_data': 'EVENT_DATAAAAA'},
        {'event_type': 'EVENT_TYPE_6', 'event_data': 'EVENT_DATAAAAA'},
        {'event_type': 'EVENT_TYPE_7', 'event_data': 'EVENT_DATAAAAA'},
        {'event_type': 'EVENT_TYPE_8', 'event_data': 'EVENT_DATAAAAA'},
        {'event_type': 'EVENT_TYPE_9', 'event_data': 'EVENT_DATAAAAA'},
        {'event_type': 'EVENT_TYPE_10', 'event_data': 'EVENT_DATAAAAA'},
        {'event_type': 'EVENT_TYPE_11', 'event_data': 'EVENT_DATAAAAA'},
    ]

    print(json.dumps(events))


if __name__ == '__main__':
    main()
