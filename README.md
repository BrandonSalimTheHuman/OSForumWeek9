To run, use this format:
python program_name.py initial_head input_file

Task 2 notes:
The instructions mention that the direction of the head is towards the innermost cylinder, and that the head position is determined through input. It also mentions that the goal of task 2 is to minimize head movement by rearranging the list of requests. Rearranging the list affects FCFS, but not the other two (SCAN & C-SCAN). This is because they do not depend on the order of requests.

This is a screenshot of the output of the file, except for this particular screenshot, I randomly shuffled the input file and then ran it through each algorithm again.

![WhatsApp Image 2024-05-11 at 21 29 47_eb99f4d4](https://github.com/BrandonSalimTheHuman/OSForumWeek9/assets/114371928/04fbf5a0-ab17-4c27-a5a0-5a950e859121)

And as expected, SCAN and C-SCAN are not affected. No matter how I rearrange the list of requests, if that's the only changeable thing, then the head movements for both SCAN and C-SCAN do not change.

For FCFS, however, the order of the requests directly impact its performance. For that reason, here is what I did to the list of requests:

1. Calculate the difference between the initial head and the innermost request, and between the initial head and the outermost request
2. If the difference between the initial head and the innermost request is smaller than the other difference. sort the list in ascending order
3. Else, sort the list in descending order

After that, regular FCFS is run using the initial head position and the rearranged list. This also means that the result will be consistent regardless of the order of requests in the original input file, as long as the numbers remain the same.
