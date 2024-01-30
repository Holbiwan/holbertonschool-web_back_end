const updateStudentGradeByCity = (students, city, newGrades) => {
if (!Array.isArray(students) || !Array.isArray(newGrades)) { 
                return [];
    } 

    const studentByCity = students.filter((student) => student.location === city)
        .map((student) => {
            const matchingGrade = newGrades.find((note) => student.id === note.studentId);
            const grade = matchingGrade ? matchingGrade.grade : 'N/A';
            
            return { ...student, grade };
        });

        return studentByCity;
};

export default updateStudentGradeByCity;
