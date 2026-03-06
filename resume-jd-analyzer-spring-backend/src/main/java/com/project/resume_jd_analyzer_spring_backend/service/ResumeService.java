package com.project.resume_jd_analyzer_spring_backend.service;

import com.project.resume_jd_analyzer_spring_backend.client.FastApiClient;
import com.project.resume_jd_analyzer_spring_backend.dto.AnalysisResponse;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

@Service
public class ResumeService {

    private final FastApiClient fastApiClient;

    public ResumeService(FastApiClient fastApiClient) {
        this.fastApiClient = fastApiClient;
    }

    public AnalysisResponse analyzeResume(MultipartFile resume, String jobDescription) throws Exception {

        if (resume.isEmpty()) {
            throw new RuntimeException("Resume file is empty");
        }

        if (!resume.getOriginalFilename().toLowerCase().endsWith(".pdf")) {
            throw new RuntimeException("Only PDF files are allowed");
        }

        if (jobDescription == null || jobDescription.trim().isEmpty()) {
            throw new RuntimeException("Job description cannot be empty");
        }

        byte[] fileBytes = resume.getBytes();
        String filename = resume.getOriginalFilename();

        return fastApiClient.analyzeResume(fileBytes, filename, jobDescription);
    }
}