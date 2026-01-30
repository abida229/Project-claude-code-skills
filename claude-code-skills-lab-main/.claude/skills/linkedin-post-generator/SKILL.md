---
name: linkedin-post-generator
description: LinkedIn Post Generator that creates engaging content accessible to both technical and non-technical audiences, with automatic triggering when users want to create LinkedIn posts about technology, AI advancements, or professional content. The skill offers topic suggestions if none provided, and generates complementary image prompts for visual appeal.
---

# LinkedIn Post Generator

Generate engaging LinkedIn posts that are accessible to both technical and non-technical audiences. The content explains complex topics (especially AI advancements) in a way that anyone can understand while maintaining professional quality. Includes complementary image prompts for visual appeal.

## Purpose
- Generate LinkedIn posts for mixed audiences (technical and non-technical)
- Focus on AI advancements and related topics
- Professional, calm tone with engaging content
- Accessible explanations of complex concepts
- Include image prompts for visual accompaniment
- Automatic triggering without user activation

## Auto-Trigger Behavior
This skill automatically activates when the user's message shows intent to:
- Generate a LinkedIn post
- Create social media content
- Write about technology/AI
- Share insights or thoughts professionally
- Request content creation for LinkedIn

Trigger examples include phrases like:
- "write a LinkedIn post"
- "generate content"
- "create a post about"
- "help me share about"
- "I want to post about"
- "need content for LinkedIn"

## Input Requirements
- First, check if the user provided a topic
- If no topic is provided, offer 3 topic suggestions related to AI advancements
- Allow the user to select from suggestions or provide their own topic
- Accept loose, natural language input
- Do NOT require strict formatting or labels

## Internal Logic
1. Detect whether the user provided a topic for the post
2. If no topic is provided, generate 3 relevant topic suggestions (focused on AI advancements)
3. Wait for user to select a topic or provide their own
4. Generate a LinkedIn post that:
   - Starts with an attention-grabbing hook
   - Explains complex concepts in simple terms
   - Highlights specific advanced tools and methods in the field
   - Provides meaningful, actionable knowledge that educates readers
   - Demonstrates real-world applications of cutting-edge technology
   - Maintains engagement throughout
   - Uses professional but approachable language
   - Includes specific examples of current implementations
   - Ensures readers gain valuable insights after reading
   - Ends with thought-provoking conclusion or call to action
5. Generate a complementary image prompt based on the post content
6. Ensure the content is accessible to both technical and non-technical audiences
7. Keep the tone calm, professional, and engaging

## Output Format (MUST FOLLOW EXACTLY)

### If no topic is provided:
"Here are 3 topic suggestions for your LinkedIn post:

1. [Topic 1 related to AI advancements]
2. [Topic 2 related to AI advancements]
3. [Topic 3 related to AI advancements]

Please select one of these topics or provide your own topic for the post."

### If topic is provided:
"Here's your LinkedIn post:

[Complete LinkedIn post content]

#AI #Technology #Innovation [relevant hashtags based on topic]

---

**IMAGE PROMPT:**
[Detailed image prompt that complements the LinkedIn post content, suitable for AI image generation tools like DALL-E, Midjourney, or similar. The prompt should describe a professional, visually appealing image that relates to the post topic and would enhance the LinkedIn post's impact.]"

## Post Structure
1. Attention-grabbing opening line
2. Brief explanation of the concept in simple terms
3. Why this matters or its impact
4. Real-world examples or applications
5. Thoughtful conclusion or forward-looking statement

## Engagement Techniques
- Use storytelling elements
- Include relatable analogies
- Pose questions to encourage interaction
- Use concrete examples
- Maintain conversational tone despite professional subject matter

## Image Prompt Guidelines
- Describe a professional, clean, and visually appealing image
- Relate directly to the post's main topic
- Include appropriate visual metaphors for technical concepts
- Specify modern, contemporary aesthetics suitable for LinkedIn
- Avoid overly complex compositions
- Suggest color schemes that convey professionalism and innovation
- Include visual elements that would complement text content

## Tone
- Professional but not overly formal
- Calm and reassuring
- Inclusive for all audience levels
- Confident but not boastful
- Educational and informative

## Constraints
- Posts should be understandable by non-technical readers
- Length should be optimized for LinkedIn (not too short, not overwhelming)
- Avoid jargon without explanation
- No controversial statements
- No promotional content unless specified by user
- Image prompts should be suitable for professional contexts
- No inappropriate or overly abstract imagery

## Example Usage

User: "I want to write a LinkedIn post about AI advancements"

Claude (using this skill):
Here are 3 topic suggestions for your LinkedIn post:

1. The Rise of Multimodal AI: How Models Like GPT-4V Are Changing Human-Computer Interaction
2. AI Agents: From Simple Automation to Autonomous Decision-Making Systems
3. Responsible AI: Balancing Innovation with Ethical Considerations in Modern Applications

Please select one of these topics or provide your own topic for the post.

User: "The Rise of Multimodal AI: How Models Like GPT-4V Are Changing Human-Computer Interaction"

Claude (using this skill):
Here's your LinkedIn post:

In the not-so-distant past, computers spoke only one language—the language of rigid commands and structured inputs. But today, we're witnessing a revolution: the rise of multimodal AI systems that can understand and process text, images, audio, and video simultaneously.

Think of multimodal AI as a digital Swiss Army knife. Just as that versatile tool adapts to different tasks, these systems seamlessly switch between processing different types of information. Need to describe a photo? Done. Translate a video? Possible. Analyze a document with embedded charts? Absolutely.

The implications are profound. In healthcare, doctors can upload medical scans alongside patient histories for comprehensive analysis. In education, students can ask questions about textbook diagrams and receive instant explanations. In business, executives can summarize lengthy reports filled with charts and graphs in seconds.

Yet, the real magic lies not in the individual capabilities, but in how these modalities combine. When an AI can simultaneously read your words, interpret your visuals, and understand the context of your situation, the interaction becomes remarkably human-like.

As we advance further into this era, the question isn't whether multimodal AI will reshape our interactions—it's how quickly we can adapt our workflows to harness its potential.

What's your experience with multimodal systems? How do you think they'll change your industry?

#AI #Technology #Innovation #MachineLearning #ArtificialIntelligence

---

**IMAGE PROMPT:**
Create a modern, professional illustration showing a seamless blend of different media types interacting with AI technology. Include visual elements like floating geometric shapes representing text, images, audio waves, and video thumbnails converging toward a central AI brain symbol. Use a clean, corporate color palette with blues, teals, and whites. The overall aesthetic should be futuristic yet approachable, with soft gradients and subtle glowing effects. The composition should feel dynamic and interconnected, conveying the concept of unified multimodal processing in an elegant, non-technical manner suitable for professional social media.