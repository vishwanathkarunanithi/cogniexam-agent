"""
Repository of 10 Diverse University Examination Question Papers from Real Curricula.
Includes Anna University, VTU, Mumbai University, JNTU, IIT Madras / NPTEL, and Velammal Autonomous.
All papers are Bloom's Revised Taxonomy calibrated across L1 to L6.
"""

SAMPLE_QUESTION_PAPERS = {
    "anna_univ_cloud": {
        "id": "1",
        "institution": "ANNA UNIVERSITY, CHENNAI",
        "department": "FACULTY OF INFORMATION AND COMMUNICATION ENGINEERING",
        "exam_type": "B.E. DEGREE EXAMINATIONS",
        "course_code": "CS8791",
        "course_title": "Cloud Computing and Distributed Systems",
        "regulation": "Regulation 2017 / 2021",
        "semester": "Semester VII / B.E. Computer Science and Engineering",
        "duration": "3 Hours",
        "max_marks": 50,
        "paper_text": """ANNA UNIVERSITY, CHENNAI
B.E. / B.Tech. DEGREE EXAMINATIONS - APRIL / MAY 2026
Seventh Semester - Computer Science and Engineering
CS8791 - CLOUD COMPUTING AND DISTRIBUTED SYSTEMS
(Regulation 2017/2021)
Time: Three Hours                                                Maximum Marks: 50

PART A - (5 x 4 = 20 Marks)
Answer ALL Questions
1. Define the CAP theorem and explain why network partition tolerance is mandatory in cloud distributed storage. [4 Marks]
2. Differentiate between Type-1 bare-metal hypervisors and Type-2 hosted hypervisors with architectural diagrams. [4 Marks]
3. Explain how consistent hashing solves hot-spot problems during dynamic node join/leave in distributed key-value stores. [4 Marks]
4. Identify the operational differences between horizontal auto-scaling and vertical auto-scaling in cloud microservices. [4 Marks]
5. State the Byzantine Generals Problem and describe the minimum number of nodes required to tolerate f faulty nodes. [4 Marks]

PART B - (2 x 15 = 30 Marks)
Answer ALL Questions
6. (a) A high-throughput banking ledger service requires strict serializability across 5 geographically distributed database replicas. Apply the Quorum Consensus algorithm (N=5, R=3, W=3). Calculate read and write latencies under network isolation, and analyze how vector clocks prevent write conflicts. [15 Marks]
7. (a) Design an enterprise-grade disaster-resilient distributed streaming pipeline capable of ingesting 100,000 telemetry events per second on Google Cloud. Justify your architectural choices for ingestion queuing, stateless compute workers, analytical storage tiers, and cross-region failover meeting RPO=0 and RTO < 30s. [15 Marks]"""
    },
    "vtu_dbms": {
        "id": "2",
        "institution": "VISVESVARAYA TECHNOLOGICAL UNIVERSITY, BELAGAVI",
        "department": "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING",
        "exam_type": "B.E. SEMESTER END EXAMINATIONS",
        "course_code": "18CS53",
        "course_title": "Database Management Systems",
        "regulation": "CBCS Scheme 2018 / 2022",
        "semester": "Fifth Semester / B.E. CSE",
        "duration": "3 Hours",
        "max_marks": 50,
        "paper_text": """VISVESVARAYA TECHNOLOGICAL UNIVERSITY, BELAGAVI
B.E. DEGREE SEMESTER END EXAMINATIONS
Fifth Semester - Computer Science and Engineering
18CS53 - DATABASE MANAGEMENT SYSTEMS
Time: 3 Hours                                                     Max Marks: 50

PART A - (5 x 4 = 20 Marks)
1. State the ACID properties of a database transaction and explain the role of the write-ahead log (WAL). [4 Marks]
2. Differentiate between B-Tree and B+ Tree index structures in terms of range query performance. [4 Marks]
3. Define Boyce-Codd Normal Form (BCNF) and distinguish it from Third Normal Form (3NF). [4 Marks]
4. Explain the phantom read anomaly and describe how Serializable isolation level prevents it. [4 Marks]
5. Illustrate conflict serializability of a schedule using a precedence (serialization) graph. [4 Marks]

PART B - (2 x 15 = 30 Marks)
6. (a) Given a relational schema R(A, B, C, D, E) with Functional Dependencies F = { A->BC, CD->E, B->D, E->A }. Determine the candidate keys of R, decompose R into BCNF, and analyze if the decomposition is lossless and dependency-preserving. [15 Marks]
7. (a) Design a comprehensive recovery protocol using Strict Two-Phase Locking (Strict 2PL) and ARIES algorithm for a distributed flight reservation system during concurrent system crashes. [15 Marks]"""
    },
    "mumbai_univ_aiml": {
        "id": "3",
        "institution": "UNIVERSITY OF MUMBAI",
        "department": "DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND DATA SCIENCE",
        "exam_type": "FINAL DEGREE EXAMINATIONS",
        "course_code": "CSC501",
        "course_title": "Artificial Intelligence and Machine Learning",
        "regulation": "Choice Based Credit and Grading System (CBCGS)",
        "semester": "Semester VI / B.E. AI&DS",
        "duration": "3 Hours",
        "max_marks": 50,
        "paper_text": """UNIVERSITY OF MUMBAI
B.E. DEGREE EXAMINATIONS - CHOICE BASED CREDIT SYSTEM
Sixth Semester - Artificial Intelligence and Data Science
CSC501 - ARTIFICIAL INTELLIGENCE AND MACHINE LEARNING
Time: 3 Hours                                                     Max Marks: 50

PART A - (5 x 4 = 20 Marks)
1. Define admissibility and consistency conditions for heuristics in the A* graph search algorithm. [4 Marks]
2. Explain the vanishing gradient problem in deep neural networks and state how ReLU activation mitigates it. [4 Marks]
3. Differentiate between Bagging and Boosting ensemble algorithms with suitable classifier examples. [4 Marks]
4. Formulate the mathematical objective function of Soft-Margin Support Vector Machines (SVM). [4 Marks]
5. State the Markov Decision Process (MDP) tuple and write the Bellman optimality equation for reinforcement learning. [4 Marks]

PART B - (2 x 15 = 30 Marks)
6. (a) Given a medical diagnostic dataset with severe class imbalance (98% negative, 2% positive), evaluate why raw classification accuracy is a misleading metric. Compute precision, recall, F1-score, and ROC-AUC. Apply SMOTE and cost-sensitive loss to solve the skew. [15 Marks]
7. (a) Design a Convolutional Neural Network (CNN) architecture with residual connections (ResNet block) for multi-label radiographic disease detection. Justify kernel sizes, pooling layers, and attention mechanisms. [15 Marks]"""
    },
    "jntu_cns": {
        "id": "4",
        "institution": "JAWAHARLAL NEHRU TECHNOLOGICAL UNIVERSITY, HYDERABAD",
        "department": "DEPARTMENT OF INFORMATION TECHNOLOGY",
        "exam_type": "B.TECH END SEMESTER EXAMINATIONS",
        "course_code": "IT702PC",
        "course_title": "Cryptography and Network Security",
        "regulation": "R18 Regulations",
        "semester": "IV Year B.Tech I Semester",
        "duration": "3 Hours",
        "max_marks": 50,
        "paper_text": """JAWAHARLAL NEHRU TECHNOLOGICAL UNIVERSITY, HYDERABAD
IV Year B.Tech I Semester Examinations
IT702PC - CRYPTOGRAPHY AND NETWORK SECURITY
Time: 3 Hours                                                     Max Marks: 50

PART A - (5 x 4 = 20 Marks)
1. Differentiate between symmetric block ciphers and asymmetric public-key cryptosystems. [4 Marks]
2. Explain the mathematical principle of Diffie-Hellman key exchange and identify the Man-in-the-Middle vulnerability. [4 Marks]
3. Define the avalanche effect in Advanced Encryption Standard (AES) and state the purpose of the S-Box substitution. [4 Marks]
4. Describe the SHA-256 compression function and explain pre-image resistance. [4 Marks]
5. Explain the role of Digital Signatures and Public Key Infrastructure (PKI) X.509 certificate chains. [4 Marks]

PART B - (2 x 15 = 30 Marks)
6. (a) Perform RSA encryption and decryption manually for primes p=11, q=13, with public exponent e=7 for message M=9. Calculate private key d using the Extended Euclidean Algorithm and verify correctness. [15 Marks]
7. (a) Design a Zero Trust Network Architecture (ZTNA) with mutual TLS (mTLS) authentication and Kerberos ticket-granting service to prevent lateral movement in a corporate intranet. [15 Marks]"""
    },
    "iit_networks": {
        "id": "5",
        "institution": "INDIAN INSTITUTE OF TECHNOLOGY / NPTEL",
        "department": "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING",
        "exam_type": "ADVANCED UNDERGRADUATE EXAMINATION",
        "course_code": "CS6003",
        "course_title": "Computer Networks and Protocol Engineering",
        "regulation": "National Programme on Technology Enhanced Learning",
        "semester": "Advanced Core Assessment",
        "duration": "3 Hours",
        "max_marks": 50,
        "paper_text": """INDIAN INSTITUTE OF TECHNOLOGY
ADVANCED UNDERGRADUATE EXAMINATION
CS6003 - COMPUTER NETWORKS AND PROTOCOL ENGINEERING
Time: 3 Hours                                                     Max Marks: 50

PART A - (5 x 4 = 20 Marks)
1. Explain the TCP three-way handshake and four-way termination process with packet sequence and control flags. [4 Marks]
2. Differentiate between Distance Vector Routing (Bellman-Ford) and Link State Routing (Dijkstra) algorithms. [4 Marks]
3. Calculate the CRC checksum for data polynomial D(x) = x^5 + x^3 + 1 using generator polynomial G(x) = x^3 + 1. [4 Marks]
4. Explain how Slow Start and Congestion Avoidance algorithms regulate TCP congestion window (cwnd) size. [4 Marks]
5. Differentiate between IPv4 and IPv6 packet headers and explain CIDR hierarchical subnet allocation. [4 Marks]

PART B - (2 x 15 = 30 Marks)
6. (a) A sender transmits 1000-byte packets over a 1 Gbps satellite link with round-trip time RTT = 250 ms. Calculate link utilization for Stop-and-Wait, Go-Back-N, and Selective Repeat protocols (window size W=128). [15 Marks]
7. (a) Design an enterprise campus software-defined network (SDN) topology with OpenFlow controllers to dynamically optimize routing paths and mitigate BGP route hijacking. [15 Marks]"""
    },
    "velammal_autonomous_web": {
        "id": "6",
        "institution": "VELAMMAL INSTITUTE OF TECHNOLOGY (AUTONOMOUS)",
        "department": "DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING",
        "exam_type": "END SEMESTER DEGREE EXAMINATIONS",
        "course_code": "CS8651",
        "course_title": "Internet Programming & Modern Web Frameworks",
        "regulation": "Regulation 2021",
        "semester": "Semester VI / B.E. CSE",
        "duration": "3 Hours",
        "max_marks": 50,
        "paper_text": """VELAMMAL INSTITUTE OF TECHNOLOGY (AUTONOMOUS)
DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING
END SEMESTER DEGREE EXAMINATIONS
CS8651 - INTERNET PROGRAMMING & MODERN WEB FRAMEWORKS
Time: 3 Hours                                                     Max Marks: 50

PART A - (5 x 4 = 20 Marks)
1. Explain the JavaScript Event Loop, microtask queue (Promises), and macrotask queue execution order. [4 Marks]
2. Differentiate between Server-Side Rendering (SSR), Client-Side Rendering (CSR), and Static Site Generation (SSG). [4 Marks]
3. Describe the Cross-Site Scripting (XSS) attack vector and state two CSP header rules for defense. [4 Marks]
4. Explain React Virtual DOM diffing reconciliation algorithm and the importance of unique stable keys. [4 Marks]
5. Differentiate between RESTful APIs and GraphQL in terms of over-fetching and network roundtrips. [4 Marks]

PART B - (2 x 15 = 30 Marks)
6. (a) Design a real-time collaborative document editing frontend using WebSockets, React hooks (useReducer, useEffect), and Conflict-Free Replicated Data Types (CRDTs). [15 Marks]
7. (a) Construct a secure Node.js/Express REST API gateway implementing OAuth 2.0 PKCE flow, JWT validation, Redis rate-limiting (sliding window), and role-based access control (RBAC). [15 Marks]"""
    },
    "cbse_board_cs": {
        "id": "7",
        "institution": "CENTRAL BOARD OF SECONDARY EDUCATION",
        "department": "SENIOR SCHOOL CERTIFICATE EXAMINATION",
        "exam_type": "ALL INDIA SENIOR SCHOOL CERTIFICATE EXAMINATION",
        "course_code": "CS083",
        "course_title": "Computer Science (Python & SQL)",
        "regulation": "CBSE Curriculum",
        "semester": "Class XII Board Examination",
        "duration": "3 Hours",
        "max_marks": 50,
        "paper_text": """CENTRAL BOARD OF SECONDARY EDUCATION
SENIOR SCHOOL CERTIFICATE EXAMINATION
CS083 - COMPUTER SCIENCE (PYTHON AND SQL)
Time: 3 Hours                                                     Max Marks: 50

PART A - (5 x 4 = 20 Marks)
1. Differentiate between mutable and immutable data types in Python with memory id demonstration. [4 Marks]
2. Explain the difference between text file and binary file operations using Python's pickle module. [4 Marks]
3. Differentiate between WHERE and HAVING clauses in SQL with practical GROUP BY queries. [4 Marks]
4. Explain packet switching vs circuit switching and define MAC address vs IP address. [4 Marks]
5. Write a recursive Python function to compute the nth Fibonacci number and state its space complexity. [4 Marks]

PART B - (2 x 15 = 30 Marks)
6. (a) Design a stack data structure in Python to evaluate a postfix mathematical expression. Trace the stack states step-by-step for the expression: '10 5 + 60 6 / * 8 -'. [15 Marks]
7. (a) A hospital database maintains tables DOCTOR(DocId, DocName, Dept, Salary) and PATIENT(PatNo, PatName, DocId, AdmitDate). Write SQL queries for equi-join, aggregate count per department, nested subquery to find highest paid doctor, and describe referential integrity constraints. [15 Marks]"""
    },
    "cambridge_ap_ca": {
        "id": "8",
        "institution": "CAMBRIDGE INTERNATIONAL / AP COMPUTER SCIENCE",
        "department": "ADVANCED PLACEMENT EXAMINATION BOARD",
        "exam_type": "AP COMPUTER SCIENCE & COMPUTER SYSTEMS",
        "course_code": "CS500",
        "course_title": "Computer Architecture & Organization",
        "regulation": "Advanced International Assessment",
        "semester": "Advanced Standing",
        "duration": "3 Hours",
        "max_marks": 50,
        "paper_text": """CAMBRIDGE INTERNATIONAL EXAMINATIONS
ADVANCED PLACEMENT EXAMINATION
CS500 - COMPUTER ARCHITECTURE & ORGANIZATION
Time: 3 Hours                                                     Max Marks: 50

PART A - (5 x 4 = 20 Marks)
1. State Amdahl's Law and calculate the maximum theoretical speedup if 75% of a program is parallelized across 8 cores. [4 Marks]
2. Differentiate between RISC (Reduced Instruction Set) and CISC (Complex Instruction Set) architectures with examples. [4 Marks]
3. Explain the three fundamental pipeline hazards: structural, data, and control hazards. [4 Marks]
4. Describe the MESI cache coherence protocol states and explain bus snooping transitions. [4 Marks]
5. Calculate Average Memory Access Time (AMAT) given L1 hit time 1ns, L1 miss rate 5%, L2 hit time 5ns, L2 miss rate 20%, and main memory penalty 80ns. [4 Marks]

PART B - (2 x 15 = 30 Marks)
6. (a) Design a 5-stage instruction pipeline (IF, ID, EX, MEM, WB) executing a loop with data dependencies. Analyze data forwarding (bypassing), hazard detection units, and branch prediction to minimize pipeline stalls. [15 Marks]
7. (a) Contrast Direct-Mapped, 4-Way Set Associative, and Fully Associative cache architectures for a 64KB cache with 64-byte blocks on a 32-bit physical memory address system. [15 Marks]"""
    },
    "srm_oops_java": {
        "id": "9",
        "institution": "SRM INSTITUTE OF SCIENCE AND TECHNOLOGY",
        "department": "DEPARTMENT OF COMPUTATIONAL INTELLIGENCE",
        "exam_type": "SEMESTER END EXAMINATIONS",
        "course_code": "18CSC202J",
        "course_title": "Object Oriented Programming in Java",
        "regulation": "Regulation 2018",
        "semester": "Semester III / B.Tech CSE",
        "duration": "3 Hours",
        "max_marks": 50,
        "paper_text": """SRM INSTITUTE OF SCIENCE AND TECHNOLOGY
SEMESTER END EXAMINATIONS - DEGREE PROGRAMMES
Third Semester - Computer Science and Engineering
18CSC202J - OBJECT ORIENTED PROGRAMMING IN JAVA
Time: 3 Hours                                                     Max Marks: 50

PART A - (5 x 4 = 20 Marks)
1. Explain the four core pillars of Object-Oriented Programming: Encapsulation, Abstraction, Inheritance, and Polymorphism. [4 Marks]
2. Differentiate between abstract classes and interfaces in Java 8+ (including default and static interface methods). [4 Marks]
3. Describe Java Memory Architecture: Stack vs Heap allocation and Garbage Collection generational phases. [4 Marks]
4. Explain checked vs unchecked exceptions and illustrate the try-with-resources statement for autocloseable streams. [4 Marks]
5. Differentiate between synchronized blocks, ReentrantLock, and volatile variables in multithreaded concurrency. [4 Marks]

PART B - (2 x 15 = 30 Marks)
6. (a) Design an extensible generic Banking Framework in Java using Factory and Observer design patterns. Implement thread-safe account balances using AtomicLong and custom checked exceptions. [15 Marks]
7. (a) Construct a Java Stream API pipeline to process a list of 100,000 transaction records: filter, map, group by transaction category, and compute summary statistics concurrently using parallel streams. [15 Marks]"""
    },
    "anna_univ_pqt": {
        "id": "10",
        "institution": "ANNA UNIVERSITY, CHENNAI",
        "department": "DEPARTMENT OF MATHEMATICS",
        "exam_type": "B.E. DEGREE EXAMINATIONS",
        "course_code": "MA8402",
        "course_title": "Probability and Queueing Theory",
        "regulation": "Regulation 2017 / 2021",
        "semester": "Semester IV / B.E. Computer Science and Engineering",
        "duration": "3 Hours",
        "max_marks": 50,
        "paper_text": """ANNA UNIVERSITY, CHENNAI
B.E. DEGREE EXAMINATIONS - APRIL / MAY 2026
Fourth Semester - Computer Science and Engineering
MA8402 - PROBABILITY AND QUEUEING THEORY
(Regulation 2017/2021)
Time: Three Hours                                                Maximum Marks: 50

PART A - (5 x 4 = 20 Marks)
Answer ALL Questions
1. Define memoryless property and prove that the exponential distribution is memoryless. [4 Marks]
2. State the necessary and sufficient conditions for a continuous stochastic process to be wide-sense stationary (WSS). [4 Marks]
3. A continuous random variable X has probability density function f(x) = k*x for 0 < x < 2. Determine constant k and compute E[X] and Var(X). [4 Marks]
4. State Little's Law for queueing systems and define each parameter (L, lambda, W). [4 Marks]
5. Differentiate between M/M/1 and M/M/c queueing models in terms of server utilization and traffic intensity. [4 Marks]

PART B - (2 x 15 = 30 Marks)
Answer ALL Questions
6. (a) In an M/M/1 queueing system at a bank counter, customers arrive according to a Poisson process with mean arrival rate lambda = 12/hour, and service time follows exponential distribution with mean service rate mu = 15/hour. Calculate: (i) Probability that the server is idle, (ii) Average number of customers in the system and in the queue, (iii) Average waiting time in the system and queue, (iv) Probability that waiting time in system exceeds 15 minutes. [15 Marks]
7. (a) A telecommunications network switch has 3 lines (M/M/3 queue). Arrival rate lambda = 6 calls/minute, each lasting an average of 30 seconds (mu = 2 calls/minute/channel). Calculate steady-state probabilities P0, P1, P2, and the probability of a call being queued. [15 Marks]"""
    }
}
