# Architecture Overview

## High-Level Flow

```
┌─────────────┐     ┌──────────────┐     ┌──────────────────┐     ┌────────────────┐     ┌─────────────┐
│  Storyboard  │────▶│ Scene Planner │────▶│ Frame Generator   │────▶│ Interpolator   │────▶│ Compositor  │
│  (YAML/CLI)  │     │              │     │ (API Adapters)    │     │ (RIFE / FILM)  │     │ (FFmpeg)    │
└─────────────┘     └──────────────┘     └──────────────────┘     └────────────────┘     └─────────────┘
```

## Design Principles

1. **Adapter pattern for APIs** — Each provider implements `BaseAPIAdapter`, making it trivial to swap or combine services.
2. **Data-driven pipeline** — The `Timeline` object flows through each stage, accumulating state.
3. **Async-first** — All I/O-bound operations are async, enabling concurrent keyframe generation.
4. **Config over code** — Resolutions, providers, rate limits live in `settings.yaml`.
5. **Fail gracefully** — Rate limiter + retry logic handle transient API errors.

## Component Responsibilities

| Component      | Role                                                        |
|----------------|-------------------------------------------------------------|
| ScenePlanner   | Parses storyboard → builds Timeline with keyframe markers   |
| FrameGenerator | Sends keyframe prompts to API → saves images to cache       |
| Interpolator   | Fills gaps between keyframes with interpolated frames        |
| Compositor     | Encodes frame sequence into video via FFmpeg                 |
| RateLimiter    | Controls API throughput to stay within provider limits       |
