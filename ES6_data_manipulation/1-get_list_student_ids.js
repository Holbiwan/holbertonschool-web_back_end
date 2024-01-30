function getListStudents(students) {
    if (!Array.isArray(students)) {
        return [];
    }
    return students.map((student) => student.id);
    }

    export default getListStudents;
