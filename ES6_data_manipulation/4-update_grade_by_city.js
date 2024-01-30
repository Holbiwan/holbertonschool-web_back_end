const updateStudentGradeByCity = (students, city, newGrade) =>
  students.map((student) => ({
    ...student,
    grade: (newGrade.find((grade) => grade.studentId === student.id) || {}).grade || 'N/A',
  })).filter((student) => student.location === city);

export default updateStudentGradeByCity;
