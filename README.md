# Getting started

## How to Build


You must have Python 2 >=2.7.9 or Python 3 >=3.4 installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=HealthOS-Python)


## How to Use

The following section explains how to use the HealthOS SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=HealthOS-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=HealthOS-Python&projectName=healthoslib)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=HealthOS-Python&projectName=healthoslib)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=HealthOS-Python&projectName=healthoslib)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from healthoslib.health_os_client import *
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=HealthOS-Python&libraryName=healthoslib.health_os_client&projectName=healthoslib)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=HealthOS-Python&libraryName=healthoslib.health_os_client&projectName=healthoslib)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke 'pip install -r test-requirements.txt'
  3. Invoke 'nosetests'

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| host | TODO: add a description |
| o_auth_access_token | The OAuth 2.0 access token to be set before API calls |



API client can be initialized as following.

```python
# Configuration parameters and credentials
host = "host"
o_auth_access_token = "o_auth_access_token" # The OAuth 2.0 access token to be set before API calls

client = HealthOSClient(host, o_auth_access_token)
```

## Class Reference

### <a name="list_of_controllers"></a>List of Controllers

* [MedicinesController](#medicines_controller)
* [LabTestsController](#lab_tests_controller)
* [GenericsController](#generics_controller)
* [FoodController](#food_controller)
* [ExercisesController](#exercises_controller)
* [DrugInteractionsController](#drug_interactions_controller)
* [DiseasesController](#diseases_controller)
* [ChatController](#chat_controller)
* [AutocompleteController](#autocomplete_controller)
* [AuthenticationController](#authentication_controller)

### <a name="medicines_controller"></a>![Class: ](https://apidocs.io/img/class.png ".MedicinesController") MedicinesController

#### Get controller instance

An instance of the ``` MedicinesController ``` class can be accessed from the API Client.

```python
 medicines_client = client.medicines
```

#### <a name="get_manufacturer"></a>![Method: ](https://apidocs.io/img/method.png ".MedicinesController.get_manufacturer") get_manufacturer

> Get a manufacturer by its id

```python
def get_manufacturer(self,
                         manufacturer_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| manufacturerId |  ``` Required ```  | Id of the manufacturer |



#### Example Usage

```python
manufacturer_id = 'manufacturer_id'

result = medicines_client.get_manufacturer(manufacturer_id)

```


#### <a name="search_manufacturers"></a>![Method: ](https://apidocs.io/img/method.png ".MedicinesController.search_manufacturers") search_manufacturers

> Search a manufacturer by its name

```python
def search_manufacturers(self,
                             manufacturer_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| manufacturerQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
manufacturer_query = 'manufacturer_query'

result = medicines_client.search_manufacturers(manufacturer_query)

```


#### <a name="get_common_side_effects"></a>![Method: ](https://apidocs.io/img/method.png ".MedicinesController.get_common_side_effects") get_common_side_effects

> Get common side effects of a medicine

```python
def get_common_side_effects(self,
                                medicine_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| medicineId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
medicine_id = 'medicine_id'

result = medicines_client.get_common_side_effects(medicine_id)

```


#### <a name="get_popular_usage"></a>![Method: ](https://apidocs.io/img/method.png ".MedicinesController.get_popular_usage") get_popular_usage

> Get popular usages of a medicine

```python
def get_popular_usage(self,
                          medicine_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| medicineId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
medicine_id = 'medicine_id'

result = medicines_client.get_popular_usage(medicine_id)

```


#### <a name="get_medicines_by_manufacturer"></a>![Method: ](https://apidocs.io/img/method.png ".MedicinesController.get_medicines_by_manufacturer") get_medicines_by_manufacturer

> Get medicines by a manufacturer

```python
def get_medicines_by_manufacturer(self,
                                      page,
                                      size,
                                      manufacturer_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Required ```  | TODO: Add a parameter description |
| size |  ``` Required ```  | TODO: Add a parameter description |
| manufacturerId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 170
size = 170
manufacturer_id = 'manufacturer_id'

result = medicines_client.get_medicines_by_manufacturer(page, size, manufacturer_id)

```


#### <a name="get_similar_medicines"></a>![Method: ](https://apidocs.io/img/method.png ".MedicinesController.get_similar_medicines") get_similar_medicines

> Get similar medicines

```python
def get_similar_medicines(self,
                              medicine_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| medicineId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
medicine_id = 'medicine_id'

result = medicines_client.get_similar_medicines(medicine_id)

```


#### <a name="get_medicine"></a>![Method: ](https://apidocs.io/img/method.png ".MedicinesController.get_medicine") get_medicine

> Get a medicine

```python
def get_medicine(self,
                     medicine_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| medicineId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
medicine_id = 'medicine_id'

result = medicines_client.get_medicine(medicine_id)

```


#### <a name="get_all_medicines"></a>![Method: ](https://apidocs.io/img/method.png ".MedicinesController.get_all_medicines") get_all_medicines

> Get all medicines

```python
def get_all_medicines(self,
                          page,
                          size)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Required ```  | TODO: Add a parameter description |
| size |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 1
size = 10

result = medicines_client.get_all_medicines(page, size)

```


#### <a name="search_medicines"></a>![Method: ](https://apidocs.io/img/method.png ".MedicinesController.search_medicines") search_medicines

> Search a medicine by name

```python
def search_medicines(self,
                         medicine_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| medicineQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
medicine_query = 'medicine_query'

result = medicines_client.search_medicines(medicine_query)

```


#### <a name="get_all_manufacturers"></a>![Method: ](https://apidocs.io/img/method.png ".MedicinesController.get_all_manufacturers") get_all_manufacturers

> Get all manufacturers

```python
def get_all_manufacturers(self,
                              page,
                              size)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Required ```  | TODO: Add a parameter description |
| size |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 1
size = 10

result = medicines_client.get_all_manufacturers(page, size)

```


#### <a name="get_alternative_medicines"></a>![Method: ](https://apidocs.io/img/method.png ".MedicinesController.get_alternative_medicines") get_alternative_medicines

> Get substitutes of a medicine

```python
def get_alternative_medicines(self,
                                  page,
                                  size,
                                  medicine_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Required ```  | TODO: Add a parameter description |
| size |  ``` Required ```  | TODO: Add a parameter description |
| medicineId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 170
size = 170
medicine_id = 'medicine_id'

result = medicines_client.get_alternative_medicines(page, size, medicine_id)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="lab_tests_controller"></a>![Class: ](https://apidocs.io/img/class.png ".LabTestsController") LabTestsController

#### Get controller instance

An instance of the ``` LabTestsController ``` class can be accessed from the API Client.

```python
 lab_tests_client = client.lab_tests
```

#### <a name="get_lab_test"></a>![Method: ](https://apidocs.io/img/method.png ".LabTestsController.get_lab_test") get_lab_test

> Get labtest by id

```python
def get_lab_test(self,
                     lab_test_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| labTestId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
lab_test_id = 'lab_test_id'

result = lab_tests_client.get_lab_test(lab_test_id)

```


#### <a name="get_all_lab_tests"></a>![Method: ](https://apidocs.io/img/method.png ".LabTestsController.get_all_lab_tests") get_all_lab_tests

> All Lab tests

```python
def get_all_lab_tests(self,
                          page,
                          size)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Required ```  | TODO: Add a parameter description |
| size |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 170
size = 170

result = lab_tests_client.get_all_lab_tests(page, size)

```


#### <a name="search_lab_tests"></a>![Method: ](https://apidocs.io/img/method.png ".LabTestsController.search_lab_tests") search_lab_tests

> Search a lab test by name

```python
def search_lab_tests(self,
                         lab_test_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| labTestQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
lab_test_query = 'lab_test_query'

result = lab_tests_client.search_lab_tests(lab_test_query)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="generics_controller"></a>![Class: ](https://apidocs.io/img/class.png ".GenericsController") GenericsController

#### Get controller instance

An instance of the ``` GenericsController ``` class can be accessed from the API Client.

```python
 generics_client = client.generics
```

#### <a name="get_generic"></a>![Method: ](https://apidocs.io/img/method.png ".GenericsController.get_generic") get_generic

> Get a generic by id

```python
def get_generic(self,
                    generic_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| genericId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
generic_id = 'generic_id'

result = generics_client.get_generic(generic_id)

```


#### <a name="get_medicines_by_generic"></a>![Method: ](https://apidocs.io/img/method.png ".GenericsController.get_medicines_by_generic") get_medicines_by_generic

> Get medicines containing the generic

```python
def get_medicines_by_generic(self,
                                 page,
                                 size,
                                 exclusive,
                                 generic_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Required ```  | TODO: Add a parameter description |
| size |  ``` Required ```  | TODO: Add a parameter description |
| exclusive |  ``` Required ```  | TODO: Add a parameter description |
| genericId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 170
size = 170
exclusive = True
generic_id = 'generic_id'

result = generics_client.get_medicines_by_generic(page, size, exclusive, generic_id)

```


#### <a name="get_all_generics"></a>![Method: ](https://apidocs.io/img/method.png ".GenericsController.get_all_generics") get_all_generics

> All generics

```python
def get_all_generics(self,
                         page,
                         size)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Required ```  | TODO: Add a parameter description |
| size |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 170
size = 170

result = generics_client.get_all_generics(page, size)

```


#### <a name="search_generics"></a>![Method: ](https://apidocs.io/img/method.png ".GenericsController.search_generics") search_generics

> Search a generic by name

```python
def search_generics(self,
                        generic_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| genericQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
generic_query = 'generic_query'

result = generics_client.search_generics(generic_query)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="food_controller"></a>![Class: ](https://apidocs.io/img/class.png ".FoodController") FoodController

#### Get controller instance

An instance of the ``` FoodController ``` class can be accessed from the API Client.

```python
 food_client = client.food
```

#### <a name="search_food_restaurants"></a>![Method: ](https://apidocs.io/img/method.png ".FoodController.search_food_restaurants") search_food_restaurants

> TODO: Add Description

```python
def search_food_restaurants(self,
                                food_restaurant_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| foodRestaurantQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
food_restaurant_query = 'food_restaurant_query'

result = food_client.search_food_restaurants(food_restaurant_query)

```


#### <a name="get_all_food_brands"></a>![Method: ](https://apidocs.io/img/method.png ".FoodController.get_all_food_brands") get_all_food_brands

> TODO: Add Description

```python
def get_all_food_brands(self,
                            page,
                            size)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Required ```  | TODO: Add a parameter description |
| size |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 1
size = 10

result = food_client.get_all_food_brands(page, size)

```


#### <a name="get_food_items_by_restaurant"></a>![Method: ](https://apidocs.io/img/method.png ".FoodController.get_food_items_by_restaurant") get_food_items_by_restaurant

> TODO: Add Description

```python
def get_food_items_by_restaurant(self,
                                     page,
                                     size,
                                     food_restaurant_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Required ```  | TODO: Add a parameter description |
| size |  ``` Required ```  | TODO: Add a parameter description |
| foodRestaurantId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 170
size = 170
food_restaurant_id = 'food_restaurant_id'

result = food_client.get_food_items_by_restaurant(page, size, food_restaurant_id)

```


#### <a name="search_food_brands"></a>![Method: ](https://apidocs.io/img/method.png ".FoodController.search_food_brands") search_food_brands

> TODO: Add Description

```python
def search_food_brands(self,
                           food_brand_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| foodBrandQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
food_brand_query = 'food_brand_query'

result = food_client.search_food_brands(food_brand_query)

```


#### <a name="get_food_item"></a>![Method: ](https://apidocs.io/img/method.png ".FoodController.get_food_item") get_food_item

> TODO: Add Description

```python
def get_food_item(self,
                      food_item_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| foodItemId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
food_item_id = 'food_item_id'

result = food_client.get_food_item(food_item_id)

```


#### <a name="get_all_food_items"></a>![Method: ](https://apidocs.io/img/method.png ".FoodController.get_all_food_items") get_all_food_items

> TODO: Add Description

```python
def get_all_food_items(self,
                           page,
                           size)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Required ```  | TODO: Add a parameter description |
| size |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 170
size = 170

result = food_client.get_all_food_items(page, size)

```


#### <a name="search_food_items"></a>![Method: ](https://apidocs.io/img/method.png ".FoodController.search_food_items") search_food_items

> TODO: Add Description

```python
def search_food_items(self,
                          food_item_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| foodItemQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
food_item_query = 'food_item_query'

result = food_client.search_food_items(food_item_query)

```


#### <a name="get_all_food_restaurants"></a>![Method: ](https://apidocs.io/img/method.png ".FoodController.get_all_food_restaurants") get_all_food_restaurants

> TODO: Add Description

```python
def get_all_food_restaurants(self,
                                 page,
                                 size)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Required ```  | TODO: Add a parameter description |
| size |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 1
size = 10

result = food_client.get_all_food_restaurants(page, size)

```


#### <a name="get_food_items_by_brand"></a>![Method: ](https://apidocs.io/img/method.png ".FoodController.get_food_items_by_brand") get_food_items_by_brand

> TODO: Add Description

```python
def get_food_items_by_brand(self,
                                page,
                                size,
                                food_brand_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Required ```  | TODO: Add a parameter description |
| size |  ``` Required ```  | TODO: Add a parameter description |
| foodBrandId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 170
size = 170
food_brand_id = 'food_brand_id'

result = food_client.get_food_items_by_brand(page, size, food_brand_id)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="exercises_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ExercisesController") ExercisesController

#### Get controller instance

An instance of the ``` ExercisesController ``` class can be accessed from the API Client.

```python
 exercises_client = client.exercises
```

#### <a name="get_exercise"></a>![Method: ](https://apidocs.io/img/method.png ".ExercisesController.get_exercise") get_exercise

> TODO: Add Description

```python
def get_exercise(self,
                     exercise_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| exerciseId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
exercise_id = 'exercise_id'

result = exercises_client.get_exercise(exercise_id)

```


#### <a name="get_all_exercises"></a>![Method: ](https://apidocs.io/img/method.png ".ExercisesController.get_all_exercises") get_all_exercises

> TODO: Add Description

```python
def get_all_exercises(self,
                          page,
                          size)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Required ```  | TODO: Add a parameter description |
| size |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 1
size = 10

result = exercises_client.get_all_exercises(page, size)

```


#### <a name="search_exercises"></a>![Method: ](https://apidocs.io/img/method.png ".ExercisesController.search_exercises") search_exercises

> TODO: Add Description

```python
def search_exercises(self,
                         exercise_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| exerciseQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
exercise_query = 'exercise_query'

result = exercises_client.search_exercises(exercise_query)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="drug_interactions_controller"></a>![Class: ](https://apidocs.io/img/class.png ".DrugInteractionsController") DrugInteractionsController

#### Get controller instance

An instance of the ``` DrugInteractionsController ``` class can be accessed from the API Client.

```python
 drug_interactions_client = client.drug_interactions
```

#### <a name="get_generics_interactions"></a>![Method: ](https://apidocs.io/img/method.png ".DrugInteractionsController.get_generics_interactions") get_generics_interactions

> TODO: Add Description

```python
def get_generics_interactions(self,
                                  generic_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| genericId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
generic_id = 'generic_id'

result = drug_interactions_client.get_generics_interactions(generic_id)

```


#### <a name="get_medicine_interactions"></a>![Method: ](https://apidocs.io/img/method.png ".DrugInteractionsController.get_medicine_interactions") get_medicine_interactions

> TODO: Add Description

```python
def get_medicine_interactions(self,
                                  medicine_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| medicineId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
medicine_id = 'medicine_id'

result = drug_interactions_client.get_medicine_interactions(medicine_id)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="diseases_controller"></a>![Class: ](https://apidocs.io/img/class.png ".DiseasesController") DiseasesController

#### Get controller instance

An instance of the ``` DiseasesController ``` class can be accessed from the API Client.

```python
 diseases_client = client.diseases
```

#### <a name="get_disease"></a>![Method: ](https://apidocs.io/img/method.png ".DiseasesController.get_disease") get_disease

> TODO: Add Description

```python
def get_disease(self,
                    disease_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| diseaseId |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
disease_id = 'disease_id'

result = diseases_client.get_disease(disease_id)

```


#### <a name="get_all_diseases"></a>![Method: ](https://apidocs.io/img/method.png ".DiseasesController.get_all_diseases") get_all_diseases

> TODO: Add Description

```python
def get_all_diseases(self,
                         page,
                         size)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| page |  ``` Required ```  | TODO: Add a parameter description |
| size |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
page = 1
size = 10

result = diseases_client.get_all_diseases(page, size)

```


#### <a name="search_diseases"></a>![Method: ](https://apidocs.io/img/method.png ".DiseasesController.search_diseases") search_diseases

> TODO: Add Description

```python
def search_diseases(self,
                        disease_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| diseaseQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
disease_query = 'disease_query'

result = diseases_client.search_diseases(disease_query)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="chat_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ChatController") ChatController

#### Get controller instance

An instance of the ``` ChatController ``` class can be accessed from the API Client.

```python
 chat_client = client.chat
```

#### <a name="get_excercises_chat"></a>![Method: ](https://apidocs.io/img/method.png ".ChatController.get_excercises_chat") get_excercises_chat

> TODO: Add Description

```python
def get_excercises_chat(self)
```

#### Example Usage

```python

result = chat_client.get_excercises_chat()

```


#### <a name="get_food_items_chat"></a>![Method: ](https://apidocs.io/img/method.png ".ChatController.get_food_items_chat") get_food_items_chat

> TODO: Add Description

```python
def get_food_items_chat(self)
```

#### Example Usage

```python

result = chat_client.get_food_items_chat()

```


#### <a name="get_medicine_chat"></a>![Method: ](https://apidocs.io/img/method.png ".ChatController.get_medicine_chat") get_medicine_chat

> TODO: Add Description

```python
def get_medicine_chat(self)
```

#### Example Usage

```python

result = chat_client.get_medicine_chat()

```


[Back to List of Controllers](#list_of_controllers)

### <a name="autocomplete_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AutocompleteController") AutocompleteController

#### Get controller instance

An instance of the ``` AutocompleteController ``` class can be accessed from the API Client.

```python
 autocomplete_client = client.autocomplete
```

#### <a name="get_exercises"></a>![Method: ](https://apidocs.io/img/method.png ".AutocompleteController.get_exercises") get_exercises

> TODO: Add Description

```python
def get_exercises(self,
                      exercise_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| exerciseQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
exercise_query = 'exercise_query'

result = autocomplete_client.get_exercises(exercise_query)

```


#### <a name="get_diseases"></a>![Method: ](https://apidocs.io/img/method.png ".AutocompleteController.get_diseases") get_diseases

> TODO: Add Description

```python
def get_diseases(self,
                     disease_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| diseaseQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
disease_query = 'disease_query'

result = autocomplete_client.get_diseases(disease_query)

```


#### <a name="get_lab_tests"></a>![Method: ](https://apidocs.io/img/method.png ".AutocompleteController.get_lab_tests") get_lab_tests

> TODO: Add Description

```python
def get_lab_tests(self,
                      lab_test_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| labTestQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
lab_test_query = 'lab_test_query'

result = autocomplete_client.get_lab_tests(lab_test_query)

```


#### <a name="get_food_items"></a>![Method: ](https://apidocs.io/img/method.png ".AutocompleteController.get_food_items") get_food_items

> TODO: Add Description

```python
def get_food_items(self,
                       food_item_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| foodItemQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
food_item_query = 'food_item_query'

result = autocomplete_client.get_food_items(food_item_query)

```


#### <a name="get_generics"></a>![Method: ](https://apidocs.io/img/method.png ".AutocompleteController.get_generics") get_generics

> TODO: Add Description

```python
def get_generics(self,
                     generic_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| genericQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
generic_query = 'generic_query'

result = autocomplete_client.get_generics(generic_query)

```


#### <a name="get_medicines"></a>![Method: ](https://apidocs.io/img/method.png ".AutocompleteController.get_medicines") get_medicines

> TODO: Add Description

```python
def get_medicines(self,
                      medicine_query)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| medicineQuery |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
medicine_query = 'medicine_query'

result = autocomplete_client.get_medicines(medicine_query)

```


[Back to List of Controllers](#list_of_controllers)

### <a name="authentication_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AuthenticationController") AuthenticationController

#### Get controller instance

An instance of the ``` AuthenticationController ``` class can be accessed from the API Client.

```python
 authentication_client = client.authentication
```

#### <a name="create_request_access_token"></a>![Method: ](https://apidocs.io/img/method.png ".AuthenticationController.create_request_access_token") create_request_access_token

> *Tags:*  ``` Skips Authentication ``` 

> TODO: Add Description

```python
def create_request_access_token(self,
                                    body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body_value = "{\n  \"grant_type\": \"client_credentials\",\n  \"client_id\": \"{{client_id}}\",\n  \"client_secret\": \"{{client_secret}}\",\n  \"scope\": \"public read write\"\n}"
body = json.loads(body_value)

result = authentication_client.create_request_access_token(body)

```

#### Errors

| Error Code | Error Description |
|------------|-------------------|
| 401 | Unauthorized |




[Back to List of Controllers](#list_of_controllers)



