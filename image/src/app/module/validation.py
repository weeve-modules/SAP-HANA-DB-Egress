"""
Validates data received by the module.
"""
from app.config import APPLICATION

allowed_data = [dict, list]

def data_validation(data):
    """Validates the incoming JSON data

    Args:
        data ([JSON Object]): [This is the request body in json format]

    Returns:
        [str, str]: [data, error]
    """
    try:
        # check data format
        if(not type(data) in allowed_data):
            return None, 'Invalid input data'
        
        labels = [label.strip() for label in APPLICATION['LABELS'].split(',')]

        # check if data contains required label
        if type(data) == dict:
            for label in labels:
                if not label in data.keys():
                    return None, 'Provided labels are not matching labels in data'

        if type(data) == list:
            for d in data:
                for label in labels:
                    if not label in d.keys():
                        return None, 'Provided labels are not matching labels in data'

        return data, None
    except Exception:
        return None, 'Invalid INPUT_LABEL'
