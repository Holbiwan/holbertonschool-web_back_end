const updateStudentGradeByCity = (students, city, newGrades) =>
  students
    .map((student) => ({
      ...student,
      grade: (newGrades.find((grade) => grade.studentId === student.id) || {}).grade || 'N/A',
    }))
    .filter((student) => student.location === city);

export default updateStudentGradeByCity;
