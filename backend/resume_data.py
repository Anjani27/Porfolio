# Anjani Kushwaha's Resume Data - Source of Truth for Python AI Agent

RESUME_DATA = {
    "identity": {
        "name": "Anjani Kushwaha",
        "location": "Lucknow, India",
        "phone": "+91-7860711908",
        "email": "anjkus27@gmail.com",
        "linkedin": "https://www.linkedin.com/in/anjani-kushwaha-245a42210",
        "github": "https://github.com/Anjani27",
        "summary": (
            "Backend and AI/ML Engineer with 1.5+ years building robust backend architectures (FastAPI, Spring Boot), "
            "Generative AI applications, and Retrieval-Augmented Generation (RAG) systems. Experienced in "
            "microservices development, REST API optimization, and agentic AI pipelines. "
            "Passionate about engineering reliable, scalable, and high-performance backend systems."
        )
    },
    "skills": {
        "programming": ["Python", "SQL", "C++", "Java"],
        "generative_ai_and_ml": [
            "LLMs", "Retrieval-Augmented Generation (RAG)", "Multi-Agent Systems",
            "LangGraph", "LangChain", "FAISS", "Transformers", "NLP", "RLHF",
            "Prompt Engineering", "Fine-tuning", "Deep Learning", "Embeddings",
            "PyTorch", "TensorFlow", "scikit-learn", "Evaluation Frameworks",
            "Model Interpretability", "Hugging Face"
        ],
        "mlops_and_systems": [
            "FastAPI", "REST APIs", "PostgreSQL", "Docker", "Vector Databases",
            "Model Deployment", "MLOps", "EDA", "Data Visualization", "Power BI",
            "Benchmarking", "Git", "GCP", "Supabase", "MCP (Model Context Protocol)",
            "TypeScript", "Streamlit", "Spring Boot"
        ]
    },
    "experience": [
        {
            "role": "Freelance Software Engineer & AI Consultant",
            "company": "Freelance",
            "location": "Remote",
            "period": "Mar 2024 – Present",
            "bullets": [
                "Developed and deployed full-stack web applications and backend microservices using Java, Spring Boot, and PostgreSQL; designed clean REST APIs and optimized database access layer.",
                "Engineered custom RAG systems, web scrapers (including LinkedIn job scrapers), and LLM pipelines using Python, FastAPI, and LangChain for various freelance clients."
            ]
        },
        {
            "role": "Software Development Engineer I (Contract)",
            "company": "Amazon via Aditi Consulting",
            "location": "Remote",
            "period": "Jun 2025 – Feb 2026",
            "bullets": [
                "Designed and executed RLHF-based model evaluation workflows across 500+ LLM outputs, applying structured performance metrics to identify reasoning failures and improve model accuracy, robustness, and instruction adherence.",
                "Designed benchmarking and evaluation frameworks to assess response quality, instruction adherence, and hallucination patterns; findings fed directly into model training cycles."
            ]
        },
        {
            "role": "LLM Python Engineer (Contract)",
            "company": "Turing",
            "location": "Remote",
            "period": "Sep 2024 – Apr 2025",
            "bullets": [
                "Executed large-scale LLM evaluation and validation workflows across Python, SQL, and ML tasks; evaluated 300+ model responses per week to improve output quality and instruction adherence.",
                "Contributed to prompt optimization workflows through systematic error analysis, improving model consistency across multi-step reasoning tasks."
            ]
        },
        {
            "role": "Data Analyst Intern",
            "company": "Quation Solutions Pvt. Ltd",
            "location": "Lucknow, India",
            "period": "Jun 2024 – Aug 2024",
            "bullets": [
                "Conducted exploratory data analysis (EDA), demand forecasting, and CPG analysis using Python and SQL across 3+ product categories; surfaced actionable insights for business stakeholders.",
                "Built Power BI dashboards adopted by the analytics team to support weekly data-driven decision-making."
            ]
        },
        {
            "role": "Software Engineer Intern",
            "company": "Microsoft India (R&D) Pvt. Ltd",
            "location": "Hyderabad, India",
            "period": "Jul 2023 – Aug 2023",
            "bullets": [
                "Designed and developed a COGS Calculator to forecast cost impact of new features over a 3-year horizon; used by the team to evaluate 10+ feature proposals.",
                "Implemented automated monitoring and alerting workflows to track cost deviations post-deployment, reducing manual review effort by ~30%."
            ]
        }
    ],
    "featured_projects": [
        {
            "title": "PromptCompiler – AI-Powered Prompt Engineering Platform",
            "period": "Jun 2026 – Present",
            "tech": ["LangGraph", "FastAPI", "Docker", "Groq (LLaMA)", "Supabase", "Next.js"],
            "liveDemo": "https://prompt-compiler-frontend.vercel.app/",
            "bullets": [
                "Built and deployed a SaaS platform using LangGraph and FastAPI that transforms user intent into structured, platform-optimized prompts through an 8-stage multi-agent AI pipeline.",
                "Engineered scalable backend with JWT authentication, usage tracking, and LLM integration via Groq-hosted LLaMA; containerized with Docker and deployed on Vercel + cloud backend."
            ]
        },
        {
            "title": "Interactive AI Assistant (RAG-based)",
            "period": "Dec 2025 – Feb 2026",
            "tech": ["LangChain", "FastAPI", "FAISS", "SSE Streaming", "Python", "LLM APIs"],
            "liveDemo": None,
            "bullets": [
                "Developed a production-grade RAG system using FastAPI, FAISS, and LLM APIs with real-time SSE streaming, achieving sub-500ms response latency for document Q&A.",
                "Built end-to-end document ingestion, chunking, embedding, and semantic retrieval pipeline; reduced hallucination rate by ~40% compared to direct LLM prompting on domain documents."
            ]
        }
    ],
    "achievements": [
        "Selected among top 6% (3K/50K) in Microsoft Engage Program'22; secured internship at Microsoft",
        "1500+ LeetCode rating",
        "5-Star Problem Solving on HackerRank",
        "Hacktoberfest contributor"
    ],
    "education": [
        {
            "degree": "B.Tech in Computer Science and Engineering",
            "institution": "Pranveer Singh Institute of Technology",
            "period": "2020 – 2024",
            "cgpa": "8.3/10"
        }
    ]
}
