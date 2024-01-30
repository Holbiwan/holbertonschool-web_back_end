export default function getStudentsByLocation(listStudents, city) {
  return Array.isArray(listStudents) ? listStudents.filter(student => student.location === city) : [];
}
