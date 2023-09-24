# Resume Optimizer

## Project Purpose

The primary aim of the **Resume Optimizer** is to generate an updated resume tailored to a specific job posting, derived from a candidate's existing resume and the given job requirements.

In the hiring process, recruiters and managers often do not read every single application document in detail. Instead, they utilize software tools that compare job listings with resumes using specific keywords, and display the ones with the highest match.

Our tool employs the same keyword-based approach, highlighting the experiences that a hiring entity values most, ensuring that the resume is tailored to each specific job listing. For instance, if a job posting emphasizes SQL experience and this experience is mentioned towards the end of an individual's resume, our tool can rearrange and emphasize this qualification to better align with the job's requirements.

Furthermore, by analyzing several job postings in a field on platforms like LinkedIn, users can identify common keywords and emphasize these in their profiles, ensuring that their experiences are articulated in a way that aligns exceptionally well with the requirements of specific jobs.

## How it Works

1. **Input**: The user provides their detailed resume and a job description.
2. **Processing**: The tool extracts keywords and pertinent information from the job description, then tailors the user's resume to highlight matching or related experiences.
3. **Output**: An optimized resume, downloadable in a plain text format.

## Code Overview

The Streamlit interface allows for easy input and displays the optimized resume. The underlying logic uses the `job_description_analyzer` module which contains two main functions:

- `analyze_desired_candidate_profile`: Extracts the desired candidate profile from the job description using language models.
  
- `refine_resume`: Refines the user's resume based on the extracted candidate profile and provided resume, emphasizing relevant experiences and qualifications.

## Prerequisites & Installation

### Required Packages

Install the necessary packages using the following pip command:

```bash
pip install openai langchain streamlit
```

### Environment Variable

For the tool to function correctly, make sure to set the `OPEN_AI_KEY` as an environment variable:

For Linux/Mac:
```bash
export OPEN_AI_KEY=your_openai_api_key
```

For Windows:
```cmd
setx OPEN_AI_KEY your_openai_api_key
```

Replace `your_openai_api_key` with your actual OpenAI API key.

## Getting Started

To run the tool locally:

1. Install the required libraries as mentioned above.
2. Ensure the `OPEN_AI_KEY` environment variable is set.
3. Run the Streamlit app using the command: `streamlit run streamlit_launcher.py`.

## Contributions & Feedback

Feel free to contribute to the codebase or provide feedback by raising issues or submitting pull requests.
