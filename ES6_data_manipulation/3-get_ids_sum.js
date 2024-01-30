// Use reduce to return the sum of the ids
function getStudentIdsSum(students) {
    return students.reduce((sum, student) => sum + student.id, 0);
  }
  
  export default getStudentIdsSum; 
