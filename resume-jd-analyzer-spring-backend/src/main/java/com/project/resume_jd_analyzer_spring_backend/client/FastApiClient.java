package com.project.resume_jd_analyzer_spring_backend.client;

import com.project.resume_jd_analyzer_spring_backend.dto.AnalysisResponse;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.http.MediaType;
import org.springframework.stereotype.Component;
import org.springframework.web.reactive.function.client.WebClient;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;

@Component
public class FastApiClient {

    private final WebClient webClient;

    public FastApiClient(WebClient webClient) {
        this.webClient = webClient;
    }

    public AnalysisResponse analyzeResume(byte[] fileBytes, String filename, String jobDescription) {

        ByteArrayResource resource = new ByteArrayResource(fileBytes) {
            @Override
            public String getFilename() {
                return filename;
            }
        };

        MultiValueMap<String, Object> body = new LinkedMultiValueMap<>();
        body.add("resume", resource);
        body.add("jobDescription", jobDescription);

        return webClient.post()
                .uri("/analyze")
                .contentType(MediaType.MULTIPART_FORM_DATA)
                .bodyValue(body)
                .retrieve()
                .bodyToMono(AnalysisResponse.class)
                .block();
    }
}
