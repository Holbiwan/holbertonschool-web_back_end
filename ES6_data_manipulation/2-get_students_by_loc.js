// getStudentsByLocation function filters an array of students
// based on the specified city and returns the filtered array.
const getStudentsByLocation = (students, city) => {
  return students.filter(student => student.location === city);
};

export default getStudentsByLocation;  
