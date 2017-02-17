# TestforEMC

1. Solution for Question 1:
Code: question_1_reverse_linked_list.py
Run:
```
  python question_1_reverse_linked_list.py 
  3, 2, 6, 3, 2, 9, 8, 
  6, 2, 3, 9, 2, 3, 8, 
```

2. Solution for Question 2:
Code: question_2.md


3. Solution for Question 3:
Run StorageSimulator RESTful API:
```
  python main.py 
  [I 170217 12:09:35 web:1971] 200 POST /api/lun/create (127.0.0.1) 1.78ms
  [I 170217 12:09:35 web:1971] 200 POST /api/lun/modify (127.0.0.1) 0.69ms
  [I 170217 12:09:35 web:1971] 200 GET /api/lun/list (127.0.0.1) 0.96ms
  [I 170217 12:09:35 web:1971] 200 POST /api/lun/delete (127.0.0.1) 0.74ms
  [I 170217 12:09:35 web:1971] 200 GET /api/lun/list (127.0.0.1) 0.63ms
```

Run Test Cases:
```
  python test_cases.py 
  Test Case 1 - Create 2 LUNs
  create lun success, the LUNs is:
  LUN: name - lun0, size - 100
  LUN: name - lun1, size - 500
  Test Case 1 - finished


  Test Case 2 - Modify LUN Size
  Modify lun success, the LUN size is changed 222
  Test Case 2 - finished


  Test Case 3 - List all the LUNs
  List LUNs success, the LUNs is:
  LUN: name - lun0, size - 222
  LUN: name - lun1, size - 500
  Test Case 3 - finished


  Test Case 4 - Delete LUN
  Delete lun success, the LUN lun0 is deleted
  List LUNs success, the LUNs is:
  LUN: name - lun1, size - 500
  detele finished
```
