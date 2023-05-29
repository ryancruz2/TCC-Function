def get_values_json(data: list):
    return list(map(create_model_json, data))

def create_model_json(json):
    return {
        "id": json["id"],
        "name": json["model"],
        "maker": json["maker_name"],
        "image": json["image_url"]
    }