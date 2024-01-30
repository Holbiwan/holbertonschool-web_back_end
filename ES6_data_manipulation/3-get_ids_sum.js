// Use reduce to return the sum of the ids
const getStudentIdsSum = (students) =>
    students.reduce((sum, student) => sum + student.id, 0);

export default getStudentIdsSum;
