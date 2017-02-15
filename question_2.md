Question 2
====

***
# Title: Create one or multiple LUNs on Storage
* Approximate Test Case Execution
* Author: Meng
* Related Bugs:
* Test Objective: Verify creating a LUN or multiple LUNs on Storage
* Setup: BUI and CLI 
* Storage Platform: Linux
* Special Configuration:
    * Create 1 LUN
        1. size: 1KB
        2. size: 999KB
        3. size: 10MB
        4. size: 1GB
        5. size: 1000GB
        6. size: 3TB
    * Create 10 LUNs, 100 LUNs, 1000 LUNs
        1. concurrently in one pool
        2. sequentially in one pool
        3. concurrently in multiple pools
    * Create 10 LUNs, 100 LUNs, 1000 LUNs
        1. On a single head of the storage
        2. On both heads of the storage
* Expected Results:
    1. Successfully created LUNs on storage (No errors or exceptions)
    2. Finished in acceptable time

***
# Title: Resize LUN Storage
* Approximate Test Case Execution
* Author: Meng
* Related Bugs:
* Test Objective: Verify resizing a LUN  on Storage
* Setup: BUI and CLI 
* Storage Platform:
* Special Configuration:
    * Resize a LUN from 100GB to 3TB
    * Resize a LUN from 100GB to 399GB
    * Resize a LUN from 100GB to 10MB
    * Resize a LUN from 3TB to 10KB
    * Resize a LUN from 5TB to 299GB
    * Resize 100 LUNs concurrently from 100GB to 10MB
* Expected Results:
    1. Successfully expanded LUNs on storage (No errors or exceptions)
    2. Finished in acceptable time

***
# Title: Export a LUN to a host
* Approximate Test Case Execution Time: 10mins
* Author:Meng
* Related Bugs:
* Test Objective: Verify exporting a LUN  on Storage
* Setup: BUI and CLI 
* Storage Platform:
* Special Configuration:
    * Export to different OSs (Linux Solaris and Windows for supported version)
    * Exported 100 LUNs concurrently
    * Exported 1000 LUNs concurrently
* Expected Results:
    1. Successfully exported LUNs to a host (No errors or exceptions)
    2. Finished in acceptable time

***
# Title: Un-export a LUN to a host
* Approximate Test Case Execution Time: 10mins
* Author:Meng
* Related Bugs:
* Test Objective: Verify un-exporting a LUN  on Storage
* Setup: BUI and CLI 
* Storage Platform:
* Special Configuration:
    * un-export to different OSs (Linux Solaris and Windows for supported version)
    * un-export 100 LUNs concurrently
    * un-export 1000 LUNs concurrently
* Expected Results:
    1. Successfully un-exported LUNs to a host (No errors or exceptions)
    2. Finished in acceptable time


*** 
# Title: Remove an un-export a LUN 
* Aproximate Test Case Execution Time: 10mins
* Author: Meng
* Related Bugs:
* Test Objective: Verify removing un-exporting a LUN 
* Setup: BUI and CLI 
* Storage Platform:
* Special Configuration:
    * Remove an un-export on different OSs (Linux Solaris and Windows for supported version)
    * Remove 100 LUNs concurrently
    * Remove 1000 LUNs concurrently
* Expected Results:
    1. Successfully removing an un-exported LUNs on a host (No errors or exceptions)
    2. Finished in acceptable time

***
# Title: Retrieve the info of a LUN
* Approximate Test Case Execution Time: 10mins
* Author: Meng
* Related Bugs:
* Test Objective: Verify results of info of a LUN 
* Setup: BUI and CLI 
* Storage Platform:
* Special Configuration:
    * Retrieve the LUN info:
        * Size
        * Used Size or Available Size
        * Online or Offline
        * Block Size(Logical/Physical)
        * Exported or Un-exported
        * Initiator or Target
        * Mountpoint
        * GUID
        * Quota
        * Reservation
* Expected Results: Retrieving the info correctly

***
# Title: Performance Test 
* Approximate Test Case Execution Time: 30 mins
* Author: Meng
* Related Bugs:
* Test Objective: Verify Performance is not impacted during the testing
* Setup: BUI and CLI 
* Storage Platform:
* Special Configuration:
    * One LUN, io size: 4KB, Read: 100%, Write: 0%, Random or Sequential
    * One LUN, io size: 4KB, Read: 0%, Write: 100%, Random or Sequential
    * One LUN, io size: 128KB, Read: 100%, Write: 0%, Random or Sequential
    * One LUN, io size: 128KB, Read: 0%, Write: 100%, Random or Sequential
    * One LUN, io size: 32MB, Read: 50%, Write: 50%, Random or Sequential
    * One LUN, io size: 32MB, Read: 50%, Write: 50%, Random or Sequential

* Expected Results:
    1. IOPs
    2. IO Latency 
    3. Any Errors
