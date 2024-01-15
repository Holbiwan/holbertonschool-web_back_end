export default function taskBlock(trueOrFalse) {
    const task = false;
    const task2 = true;
  
    let localTask = task;
    let localTask2 = task2;
  
    if (trueOrFalse) {
      // eslint-disable-next-line
      localTask = true;
      localTask2 = false;
  
      // Returns values of local variables inside the block   
      return [localTask, localTask2];
    }
  
    // Returns values of variables declared outside the block    
    return [task, task2];
  }
  