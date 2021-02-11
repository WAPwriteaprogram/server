-- CREATE DATABASE fakedb_wap;

CREATE TABLE users(
    user_id BIGSERIAL,
    username VARCHAR(128) PRIMARY KEY,
    email VARCHAR(254) NOT NULL UNIQUE,
    password_hashed TEXT NOT NULL,
    privilage SMALLINT NOT NULL,
    courses_joined INTEGER []
);

CREATE TABLE problem_pool(
    problem_id BIGSERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    tags TEXT [],
    solution TEXT,
    output_stream VARCHAR(255) NOT NULL, -- stdout/filename.txt
    input TEXT [], -- if from stdin
    arguments TEXT [],
    expected_output TEXT [] NOT NULL
);

CREATE TABLE courses(
    id SERIAL,
    course_code INTEGER PRIMARY KEY,
    course_name VARCHAR(128) NOT NULL,
    studets VARCHAR(128) [],
    instructors VARCHAR(128) [],
    assignments INTEGER []
);

CREATE TABLE assignment(
    assignment_code INTEGER NOT NULL,
    course_code INTEGER NOT NULL REFERENCES courses(course_code),
    assignment_name VARCHAR(128) NOT NULL,
    due TIMESTAMP WITHOUT TIME ZONE,
    public BOOLEAN NOT NULL,
    starts TIMESTAMP WITHOUT TIME ZONE,
    questions BIGINT [] NOT NULL,
    UNIQUE(assignment_code, course_code)
);

CREATE TABLE question(
    assignment_code INTEGER NOT NULL,
    course_code INTEGER NOT NULL REFERENCES courses(course_code),
    problem_id BIGINT NOT NULL REFERENCES problem_pool(problem_id),
    max_marks FLOAT NOT NULL,
    test_case_weightage FLOAT [] NOT NULL,  -- default=0(test case wouldnt matter), can be 0.5x, 0.25x
    UNIQUE(assignment_code, course_code, problem_id)
);

CREATE TABLE user_submission(
    problem_id BIGINT NOT NULL REFERENCES problem_pool(problem_id),
    assignment_code INTEGER NOT NULL,
    course_code INTEGER NOT NULL REFERENCES courses(course_code),
    user_username VARCHAR(128) NOT NULL REFERENCES users(username),
    user_solution TEXT,
    test_case_satisfied BOOLEAN [] NOT NULL,
    marks FLOAT NOT NULL,
    user_query TEXT,
    UNIQUE(problem_id, assignment_code, user_username, course_code)
);