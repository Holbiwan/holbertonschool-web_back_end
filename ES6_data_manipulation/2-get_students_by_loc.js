export default function getStudentsByLocation(students, city) {
  console.log("Received list of students:", students);
  
  const studentsInCity = students.filter(student => student.location === city);
  
  console.log("Students in the specific city:", studentsInCity);
  
  return studentsInCity;
}
