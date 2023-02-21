import json

# CO2 g per km
activity_emissions = {'IN_PASSENGER_VEHICLE': 170,
                      'FLYING': 300,
                      'IN_BUS': 100,
                      'MOTORCYCLING': 100,
                      'IN_TRAIN': 100,
                      'IN_SUBWAY': 100,
                      'WALKING': 0,
                      'CYCLING': 0,
                      'RUNNING': 0,
                      'UNKNOWN_ACTIVITY_TYPE': 0}


# given a dictionary of activities and their km, return sum of CO2 in KG
def computeCO2(activities_l):
    total = 0.0
    for key in activities_l:
        # the try is to avoid errors if a key is not present in emissions
        try:
            total = total + activities_l[key] * activity_emissions[key]
        except KeyError:
            pass
    return round(total/1000.0)


def safe_extract(activity_list, activity):
    if activity in activity_list:
        return activity_list[activity]
    else:
        return 0


def add_activity(activities_l, activity):
    activity_type_l = activity[1]
    distance_l = activity[2]
    if activity_type_l in activities_l:
        activities_l[activity_type_l] = activities_l[activity_type_l] + distance_l
    else:
        activities_l[activity_type_l] = distance_l


def process_segment(activity_segment_l):
    try:
        activity_type = activity_segment_l['activityType']
        date = activity_segment_l['duration']['startTimestamp'][0:10]
        distance = round(float(activity_segment_l['distance']) / 1000)
        confidence = activity_segment_l['confidence']
        # print(f"{date}: {activity_type} {distance}  {confidence}")
        return [date, activity_type, distance, confidence]
    except KeyError:
        pass
    return None


# given a json file, return list of activities
# return list of elements: 2018-05-26 WALKING 0  HIGH
def process_file(file_path):
    activities_month = []
    activity_sum_month = {}
    with open(file_path, "r") as file:
        data = json.load(file)
    # first level: dictionary with a single entry
    tl_objects = data["timelineObjects"]
    # tl_objects is a list
    for tl_object in tl_objects:
        # each object of the list is a single entry
        if 'activitySegment' in tl_object.keys():
            activity_segment = tl_object['activitySegment']
            processed_segment = process_segment(activity_segment)
            if processed_segment:
                activities_month.append(processed_segment)
    return activities_month


# input list of activities
# return dictionary with added km
def compress_month(activities_month):
    sum_month = {}
    for activity in activities_month:
        activity_type = activity[1]
        distance = activity[2]
        if activity_type in sum_month.keys():
            sum_month[activity_type] = sum_month[activity_type] + distance
        else:
            sum_month[activity_type] =  distance

    return sum_month
