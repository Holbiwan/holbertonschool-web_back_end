export default function getStudentsByLocation(students, city) {
  console.log("Liste des étudiants reçue :", students);
  
  const studentsInCity = students.filter(student => student.location === city);
  
  console.log("Étudiants dans la ville spécifique :", studentsInCity);
  
  return studentsInCity;
}
