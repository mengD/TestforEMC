Title: Create a or multiple LUNs on Storage

Approximate Test Case Execution Time: 30 mins

Author:Meng

Related Bugs:

Test Objective: Verify creating a LUN or multiple LUNs on Storage

Setup: BUI and CLI 

Storage Platform:

Special Configuration:
    1.Create 10 LUNs concurrently  
    2.Create 100 LUNs concurrently 
    3.Create 1000 LUNs concurrently
    4. In the same pool
    5. Cross different pools 
    6. On a single head of the storage
    7. On both heads of the storage

Expected Results: Successfully created LUNs on storage (No errors or exceptions)



Title: Resize LUN Storage

Approximate Test Case Execution Time: 10mins

Author:Meng

Related Bugs:

Test Objective: Verify resizing a LUN  on Storage

Setup: BUI and CLI 

Storage Platform:

Special Configuration:

Expected Results: Successfully expanded LUNs on storage (No errors or exceptions)


Title: Export a LUN to a host

Approximate Test Case Execution Time: 10mins

Author:Meng

Related Bugs:

Test Objective: Verify exporting a LUN  on Storage

Setup: BUI and CLI 

Storage Platform:

Special Configuration:
    1.Export to different OSs (Linux Solaris and Windows for supported version)
    2. exported 100 LUNs concurrently
    3.exported 1000 LUNs concurrently

Expected Results: Successfully exported LUNs to a host (No errors or exceptions)


Title: Un-export a LUN to a host

Approximate Test Case Execution Time: 10mins

Author:Meng

Related Bugs:

Test Objective: Verify un-exporting a LUN  on Storage

Setup: BUI and CLI 

Storage Platform:

Special Configuration:
    1.un-export to different OSs (Linux Solaris and Windows for supported version)


Expected Results: Successfully un-exported LUNs to a host (No errors or exceptions)


Title: Remove an un-export a LUN 

Approximate Test Case Execution Time: 10mins

Author:Meng

Related Bugs:

Test Objective: Verify removing un-exporting a LUN 

Setup: BUI and CLI 

Storage Platform:

Special Configuration:
    1. removing an un-export on different OSs (Linux Solaris and Windows for supported version)


Expected Results: Successfully removing an un-exported LUNs on a host (No errors or exceptions)


Title: Retrieve the info of a LUN

Approximate Test Case Execution Time: 10mins

Author:Meng

Related Bugs:

Test Objective: Verify results of info of a LUN 

Setup: BUI and CLI 

Storage Platform:

Special Configuration:
    1. size
    2. export
    3. initiator/target
    4. Quota/Reservation

Expected Results: Retrieving the info correctly


Title: Performance Test 

Approximate Test Case Execution Time: 30 mins

Author:Meng

Related Bugs:

Test Objective: Verify Performance is not impacted during the testing

Setup: BUI and CLI 

Storage Platform:

Special Configuration:

    Create 100 LUNs and 1000 LUNs and check the following performance measurement
    1. IOPs
    2. IO Latency 

Expected Results: IOPs and IO Latency 
