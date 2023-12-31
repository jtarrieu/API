import traceback

from src.services.data import (get_kaggle_data, load_iris_dataset, processing_dataset, split_dataset, train_dataset,
                               predict, get_firestore_data, update_firestore_data)
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/data")
def get_data():
    try:
        get_kaggle_data()
    except:
        return "Error: couldn't get download data."

    return "Kaggle data downloaded successfully"


@ router.get("/data/load")
def load_data_as_json():
    dataset = load_iris_dataset()
    if "error" in dataset:
        raise HTTPException(status_code=404, detail=dataset["error"])
    return dataset


@router.get("/data/process")
def get_processed_iris_dataset():
    processed_dataset = processing_dataset()
    if "error" in processed_dataset:
        raise HTTPException(status_code=404, detail=processed_dataset["error"])
    return processed_dataset


@router.get("/data/split")
def split_iris_dataset():
    result = split_dataset()
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/data/train")
def train_iris_dataset():
    result = train_dataset()
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/data/predict")
def predict_iris_dataset():
    result = predict()
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/data/get-firestore")
def get_firestore():
    result = get_firestore_data()
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/data/update-firestore")
def update_firestore():
    #here we change the n_estimators parameter
    result = update_firestore_data('n_estimators',300)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/data/add-firestore")
def add_parameter():
    # here we add a useless parameter
    result = update_firestore_data('test_param',400)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result