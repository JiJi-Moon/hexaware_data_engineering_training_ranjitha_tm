// use database
use course_tracker;

// create collections
db.createCollection("students");
db.createCollection("courses");
db.createCollection("enrollments");
db.createCollection("progress");

// insert students
db.students.insertMany([
  { student_id: 1, name: "ranjitha", email: "ranjitha@gmail.com" },
  { student_id: 2, name: "arun", email: "arun@gmail.com" },
  { student_id: 3, name: "meena", email: "meena@gmail.com" }
]);

// insert courses
db.courses.insertMany([
  { course_id: 1, course_name: "deep learning", instructor: "dr. kumar" },
  { course_id: 2, course_name: "data science", instructor: "dr. priya" },
  { course_id: 3, course_name: "cloud computing", instructor: "mr. ravi" }
]);

// insert enrollments
db.enrollments.insertMany([
  { enrollment_id: 1, student_id: 1, course_id: 1, enrollment_date: "2026-01-10" },
  { enrollment_id: 2, student_id: 1, course_id: 2, enrollment_date: "2026-01-12" },
  { enrollment_id: 3, student_id: 2, course_id: 3, enrollment_date: "2026-01-15" }
]);

// insert progress
db.progress.insertMany([
  { progress_id: 1, enrollment_id: 1, completion_percentage: 40, last_updated: "2026-02-01" },
  { progress_id: 2, enrollment_id: 2, completion_percentage: 75, last_updated: "2026-02-05" },
  { progress_id: 3, enrollment_id: 3, completion_percentage: 20, last_updated: "2026-02-03" }
]);

// indexes
db.students.createIndex({ student_id: 1 });
db.courses.createIndex({ course_id: 1 });
db.enrollments.createIndex({ student_id: 1 });
db.enrollments.createIndex({ course_id: 1 });

// feedback collection
db.feedback.insertMany([
  { student_id: 1, course_id: 1, rating: 5, feedback: "very useful course" },
  { student_id: 1, course_id: 2, rating: 4, feedback: "good content and teaching" },
  { student_id: 2, course_id: 3, rating: 3, feedback: "average experience" },
  { student_id: 3, course_id: 1, rating: 5, feedback: "excellent explanation" },
  { student_id: 4, course_id: 4, rating: 2, feedback: "needs improvement" }
]);

// feedback indexes
db.feedback.createIndex({ student_id: 1 });
db.feedback.createIndex({ course_id: 1 });