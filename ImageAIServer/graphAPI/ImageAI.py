from imageai.Detection import ObjectDetection
import os

MIN_PROBABILITY = 15

def getCarAndMotorcycleCoordsFromImageResnet(image_name):
    execution_path = os.getcwd()

    #FIXME adjust image path
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    # detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()

    custom_objects = detector.CustomObjects(car=True, motorcycle=True)
    detections = detector.detectCustomObjectsFromImage(custom_objects=custom_objects, input_image=os.path.join(execution_path ,image_name), output_image_path=os.path.join(execution_path , image_name.split(".")[0] + "_processed.jpg"), minimum_percentage_probability=MIN_PROBABILITY)

    coords = []

    for eachObject in detections:
        coords.append(eachObject['box_points'].tolist())

    return coords

def getCoordsFromImageResnet(image_name):
    execution_path = os.getcwd()

    #FIXME adjust image path
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    pdb.set_trace()

    custom_objects = detector.CustomObjects(car=True, motorcycle=True, cell_phone=True, bus=True, truck=True, parking_meter=True, mouse=True, bowl=True, suitcase=True)
    detections = detector.detectCustomObjectsFromImage(custom_objects=custom_objects, input_image=os.path.join(execution_path ,image_name), output_image_path=os.path.join(execution_path, image_name[:-4] + "_processed.jpg"), minimum_percentage_probability=MIN_PROBABILITY)
    # detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path ,image_name), output_image_path=os.path.join(execution_path, image_name[:-4] + "_processed.jpg"), minimum_percentage_probability=MIN_PROBABILITY)

    coords = []

    for eachObject in detections:
        coords.append(eachObject['box_points'].tolist())

    return coords

def getCoordsFromImageResnetCalibrate(image_name):
    execution_path = os.getcwd()

    #FIXME adjust image path
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()

    custom_objects = detector.CustomObjects(car=True, motorcycle=True, cell_phone=True, truck=True, parking_meter=True, mouse=True, bowl=True, suitcase=True)
    detections = detector.detectCustomObjectsFromImage(custom_objects=custom_objects, input_image=os.path.join(execution_path ,image_name), output_image_path=os.path.join(execution_path, image_name[:-4] + "_processed.jpg"), minimum_percentage_probability=MIN_PROBABILITY)
    # detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path ,image_name), output_image_path=os.path.join(execution_path, image_name[:-4] + "_processed.jpg"), minimum_percentage_probability=MIN_PROBABILITY)

    coords = []

    for eachObject in detections:
        coords.append(eachObject['box_points'].tolist())

    return coords


