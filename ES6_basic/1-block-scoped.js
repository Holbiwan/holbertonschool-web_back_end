export default function taskBlock(trueOrFalse) {
    const task = false;
    const task2 = true;

    if (trueOrFalse) {
        // eslint-disable-next-line
        const localTask = true;
        const localTask2 = false;

       // Returns values of local variables inside the block   
        return [localTask, localTask2];
    }
       // Returns values of variables declared outside the block    
      return [task, task2];
    }
