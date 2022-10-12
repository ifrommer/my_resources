1. Assignments in the coding classes (including IDM) should often by modules that my checker code calls and tests.  
2. Traffic simulator to test out my idea of finding the mean speed and traveling at it to smooth out traffic.  You'd need a lot of things:
- little car objects:
  - methods - appear, move, disapper
  - attributes - position, speed, speed distribution parameters - there might be a few, (lane)
    - figuring out the speed distriution could be tricky
    - also, how about car reacting to car in front, it'd need a behavior to slow down if it approached the next car, could get complicated - if you're within some distance, you slow down to match the speed of the car in front of you
      - we want to log these deceleration events
