package com.project.resume_jd_analyzer_spring_backend.controller;

import com.project.resume_jd_analyzer_spring_backend.dto.AnalysisResponse;
import com.project.resume_jd_analyzer_spring_backend.service.ResumeService;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "http://localhost:5173")
public class ResumeController {

    private final ResumeService resumeService;

    public ResumeController(ResumeService resumeService) {
        this.resumeService = resumeService;
    }

    @PostMapping("/analyze")
    public AnalysisResponse analyzeResume(
            @RequestParam("resume") MultipartFile resume,
            @RequestParam("jobDescription") String jobDescription
    ) throws Exception {

        return resumeService.analyzeResume(resume, jobDescription);
    }
}
