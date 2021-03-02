-- CREATE DATABASE fakedb_wap;

CREATE TABLE users(
    user_id BIGSERIAL,
    username VARCHAR(128) PRIMARY KEY,
    email VARCHAR(254) NOT NULL UNIQUE,
    password_hashed TEXT NOT NULL,
    privilege SMALLINT NOT NULL,
    section VARCHAR(10),
    batch VARCHAR(10)
);

CREATE TABLE courses(
    id SERIAL,
    course_code VARCHAR(10) PRIMARY KEY,
    course_name VARCHAR(128) NOT NULL
);

CREATE TABLE courses_users(
    course_code VARCHAR(10) NOT NULL REFERENCES courses(course_code),
    users VARCHAR(128) NOT NULL REFERENCES users(username),
    UNIQUE(course_code, users)
);

CREATE TABLE problem_pool(
    problem_id BIGSERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    solution TEXT,
    output_stream VARCHAR(255) NOT NULL, -- stdout/filename.txt
    creator VARCHAR(128) NOT NULL REFERENCES users(username)
);

CREATE TABLE problem_pool_tags(
    problem_id BIGINT NOT NULL REFERENCES problem_pool(problem_id),
    tags TEXT NOT NULL,
    UNIQUE(problem_id, tags)
);
CREATE TABLE problem_pool_test_case(
    test_case_id INTEGER NOT NULL,
    problem_id BIGINT NOT NULL REFERENCES problem_pool(problem_id),
    expected_output TEXT NOT NULL,
    input TEXT, -- if from stdin
    arguments TEXT,
    UNIQUE(problem_id, test_case_id)
);


CREATE TABLE assignment(
    assignment_code INTEGER NOT NULL,
    course_code VARCHAR(10) NOT NULL REFERENCES courses(course_code),
    assignment_name VARCHAR(128) NOT NULL,
    public BOOLEAN NOT NULL,
    starts TIMESTAMP WITHOUT TIME ZONE,
    due TIMESTAMP WITHOUT TIME ZONE,
    UNIQUE(assignment_code, course_code)
);

CREATE TABLE question(
    question_id BIGINT PRIMARY KEY REFERENCES problem_pool(problem_id),
    assignment_code INTEGER NOT NULL,
    course_code VARCHAR(10) NOT NULL REFERENCES courses(course_code),
    problem_id BIGINT NOT NULL REFERENCES problem_pool(problem_id),
    max_marks FLOAT NOT NULL
);

CREATE TABLE question_test_case(
    test_case_id INTEGER NOT NULL,
    question_id BIGINT NOT NULL REFERENCES question(question_id),
    weightage FLOAT NOT NULL, -- default=0(test case wouldnt matter), can be 0.5x, 0.25x
    public BOOLEAN NOT NULL,
    UNIQUE(question_id, test_case_id)
);

CREATE TABLE user_submission(
    question_id BIGINT NOT NULL REFERENCES question(question_id),
    user_username VARCHAR(128) NOT NULL REFERENCES users(username),
    user_solution TEXT,
    marks FLOAT NOT NULL,
    user_query TEXT,
    UNIQUE(question_id, user_username)
);

CREATE TABLE user_submission_test_case_satisfied(
    test_case_id INTEGER NOT NULL,
    question_id BIGINT NOT NULL REFERENCES question(question_id),
    user_username VARCHAR(128) NOT NULL REFERENCES users(username),
    test_case_satisfied BOOLEAN NOT NULL,
    UNIQUE(question_id, user_username, test_case_id)
);

-- CREATE TABLE sessions(
--     id INTEGER PRIMARY KEY,
--     session_id VARCHAR(255) UNIQUE,
--     data BYTEA,
--     expiry TIMESTAMP
-- );





-- update users
-- set privilege=2
-- where username='user1';
