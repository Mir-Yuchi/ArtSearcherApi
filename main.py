import time
import requests

API_BASE_URL = "https://collectionapi.metmuseum.org/public/collection/v1/"
API_BASE_OBJECTS_URL = API_BASE_URL + "objects/"
API_BASE_SEARCH_URL = API_BASE_URL + "search?q="


def get_all_objects() -> dict:
    response = requests.get(API_BASE_URL + "objects")
    return response.json() if response.status_code == 200 else response.status_code


def get_object_detail(object_id):
    response = requests.get(f"{API_BASE_OBJECTS_URL}{object_id}")
    return response.json() if response.status_code == 200 else response.status_code


def object_searcher():
    object_name = input("Write what you want to find: ")
    response = requests.get(API_BASE_SEARCH_URL + object_name)
    return response.json() if response.status_code == 200 else response.status_code


def run():
    object_ids = object_searcher()["objectIDs"]
    if not object_ids:
        print("COULDN'T FIND OBJECT :(")
        return
    total_ids = len(object_ids)
    object_id = 0
    while object_id <= total_ids:
        object_info = get_object_detail(object_ids[object_id])
        print(50 * "-")
        print("Artwork was acquired at:", object_info["accessionYear"], "\nLink to image:", object_info["primaryImage"],
              "\nName given to a work of art:", object_info["title"], "\nDepartment is:", object_info["department"],
              "\nArt is about", object_info["culture"], object_info["objectName"],
              "\nArt located in:", object_info["repository"], "\nLink to Wikidata:", object_info["objectWikidata_URL"])
        if total_ids == 1:
            print("\t\t\t\t\tNO MORE ARTS :(\n"
                  "\t\t\t\t\tTHANK YOU FOR USING :)", )
            return
        need_continue = input("\tDo you want to see next art of the same object? (Yes/No): ").lower()
        if need_continue == "yes":
            object_id += 1
            time.sleep(2)
        elif need_continue == "no":
            print("\t\t\t\t\tTHANK YOU FOR USING :)", )
            break
        else:
            print("\t\t\t\t\tYOU DID SOMETHING WRONG!!!")
            break


run()
