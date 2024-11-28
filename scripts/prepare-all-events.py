import json


def main():
    events = [
        {'event_type': 'EVENT_TYPE_1', 'event_data': {'d': 1, 'w': 22}},
        {'event_type': 'EVENT_TYPE_2', 'event_data': {'d': 21, 'w': 222}},
        {'event_type': 'EVENT_TYPE_3', 'event_data': {'d': 31, 'w': 322}},
        {'event_type': 'EVENT_TYPE_4', 'event_data': {'d': 41, 'w': 422}},
        {'event_type': 'EVENT_TYPE_5', 'event_data': {'d': 41, 'w': 422}},
        {'event_type': 'EVENT_TYPE_6', 'event_data': {'d': 41, 'w': 422}},
        {'event_type': 'EVENT_TYPE_7', 'event_data': {'d': 41, 'w': 422}},
        {'event_type': 'EVENT_TYPE_8', 'event_data': {'d': 41, 'w': 422}},
        {'event_type': 'EVENT_TYPE_9', 'event_data': {'d': 41, 'w': 422}},
        {'event_type': 'EVENT_TYPE_10', 'event_data': {'d': 41, 'w': 422}},
        {'event_type': 'EVENT_TYPE_11', 'event_data': {'d': 41, 'w': 422}},
    ]

    print(json.dumps(events))


if __name__ == '__main__':
    main()