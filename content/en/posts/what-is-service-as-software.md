---
date: '2026-04-10T16:33:00+02:00'
draft: false
title: 'Service as software: The software is the work'
slug: 'what-is-service-as-software'
translationKey: 'what-is-service-as-software'
tags:
  - ai
  - software
  - strategy
  - innovation
  - management
_gemini:
  key_theme: Service as software is a way for software-based-services to scale and retain high margins, without being constrained by labour cost (like with BPM) and without being constrained by software that is not able to handle changes (like RPA). It is enabled by AI agents.
  key_insights:
    - Software is the area where AI is the most widespread. It is because software is predominantly about intellectual work and less so about judgement. Areas where AI agents are going to grow fastest are the ones where intellectual work is majority of work.
    - \"Jobs to be done\" framework is a great tool to identify which areas of en enterprise are a good fit for AI agents.
    - Alternatives to service-as-software:
      - Software-as-a-Service (SaaS) - "Here is a tool. Do the work.".
        - How it works? Renting access to cloud-based tools; Salesforce, Google Workspace, Notion, Figma.
        - Very low cost of distribution.
        - Very high margins.
        - Limitation: SaaS does only what is was designed to do. It is not flexible and requires development of new features to handle new scenarios. It requires human employees to do the thinking.
      - Tech-Enabled Services — "We will do the work using our tools".
        - How it works? Companies use proprietary software to make their own human employees more efficient at delivering a service to you.
        - High customer satisfaction because the customer buys an actual outcome.
        - Limitation: Gross margins are lower than SaaS, and managing human workforce introduces complexity, errors, and HR overhead.
      - Robotic Process Automation (RPA) — "The software will do the work, but only if nothing changes."
        - How it works? Tools like UiPath or Zapier allowed companies to automate highly repetitive tasks.
        - A glimpse into software replacing human labor.
        - RPA requires rigid rules, structured data, and unchanging environments. If an invoice format changes slightly, or an email is phrased ambiguously, the RPA bot breaks and a human has to step in. It couldn't handle unstructured reality.
      - AI Agents & Service-as-Software — "The software is the labor."
        - How it works? Large Language Models introduced reasoning, adaptability, and the ability to process unstructured data (text, images, messy human requests). AI Agents wrap these models in autonomous loops, allowing them to plan, use tools, and execute multi-step workflows.
        - You don't buy the software to use it. You hire the software to do the job. (e.g., You don't buy an AI coding tool, you hire an AI software engineer like Devin; you don't buy legal software, you hire an AI paralegal).
        - Software can handle the fuzzy, ambiguous, non-deterministic tasks that previously required human cognition.
    - ...
  sources:
    - https://sequoiacap.com/article/services-the-new-software/
    - https://www.thoughtworks.com/insights/blog/generative-ai/service-as-software-a-new-economic-model-for-age-of-ai-agents
    - https://michaelburnett3.substack.com/p/from-saas-to-service-as-software
    - https://www.3one4capital.com/blogs/signals-from-software-as-a-service-to-service-as-software-rethinking-saas-in-the-ai-era
    - https://www.hfsresearch.com/research/saas-services-as-software/
    - https://mkcg.pl/posts/ai-changes-jtbd/
  word_count_target: 800
---

The software industry is entering a phase where the boundary between a tool and a worker is dissolving. For two decades, the dominant economic model for digital innovation was Software-as-a-Service (SaaS). We built platforms that acted as force multipliers for human employees. You bought a license for Salesforce or Figma so that your sales team or designers could be more efficient. The work itself, however, remained a human-led endeavor. The software was the infrastructure; the human was the labor.

This is changing. We are moving toward a model where the software is the labor. This paradigm, often referred to as Service-as-Software, represents a fundamental shift in how organizations procure value. Instead of buying access to a tool to do the work, companies are beginning to "hire" software to deliver the outcome directly. This transition is not merely a technological iteration but a restructuring of the global services economy.

### The predecessors: SaaS and Tech-Enabled Services

Understanding the distinction between Service-as-Software and its predecessors requires examining the models it seeks to replace. Traditional SaaS was revolutionary because it decoupled software from physical infrastructure. It offered high margins and low distribution costs, but its scalability was still tied to the customer's ability to provide human labor to operate the tools. A company with more customers needed more licenses, and consequently, more employees.

Then there are tech-enabled services. This model, often seen in business process outsourcing (BPO) or consulting, uses proprietary software to make human employees more efficient at delivering a service. While this provides a better experience for the customer, who is buying a finished product rather than a tool, it is economically constrained. The gross margins are lower than SaaS, and the operation is still limited by the complexities of managing a human workforce. Scaling requires hiring, which introduces overhead and linear costs.

Robotic Process Automation (RPA) attempted to bridge this gap by automating repetitive tasks. It offered a glimpse into a world where software replaces human labor, but it was fragile. RPA requires rigid rules and structured environments. It functions as a sequence of hard-coded scripts. If an invoice format changes or an email arrives with ambiguous phrasing, the RPA bot fails, requiring a human to intervene. RPA could not handle the "messy" reality of unstructured business data.

### The Service-as-Software model

Service-as-Software, enabled by AI agents, circumvents these limitations by introducing reasoning into the workflow. Unlike RPA, which executes instructions, AI agents operate by pursuing goals. They can process unstructured text, images, and non-deterministic requests. They adapt to changes in their environment without manual reprogramming.

In this model, you do not buy an AI tool for your legal team; you hire an AI paralegal. You do not buy an IDE extension for your developers; you hire an AI software engineer. The shift is from selling a productivity multiplier to selling the work product itself [^1]. This allows vendors to target payroll and outsourced services budgets—which are orders of magnitude larger than IT budgets. It is a migration from the IT budget to the services budget.

The economic implications are significant. Because the marginal cost of compute (inference) is collapsing, the cost of "digital labor" is falling much faster than human labor ever could. While traditional SaaS has near-zero marginal costs, Service-as-Software does have higher COGS due to GPU requirements. However, unlike human services, these costs do not scale linearly with headcount. Once an agentic workflow is established, it can handle a near-infinite volume of tasks with software-like scalability [^2].

### Identifying the jobs to be done

For leadership, the challenge is identifying where this model provides the most value. We can look at this through the lens of [How AI changes our jobs to be done](/posts/ai-changes-jtbd/). Much of the corporate structure is composed of intermediate steps—reports, documentation, coordination—that exist only because we lacked the technology to achieve the outcome directly.

Service-as-Software works best in areas where intellectual work is the majority of the task, but the "judgement" requirements are manageable. Software engineering, legal review, and financial reporting are prime candidates because they are predominantly about intellectual synthesis and rules-based logic. As I noted in [Is AI more tech? Or less?](/posts/ai-removes-tech-from-our-lives/), we are developing the ability to mix algorithmic-rigid systems with human-flexible decision points. Service-as-Software allows us to automate the "intelligence" while reserving human judgment for the most ambiguous or high-stakes scenarios [^3].

### From operator to orchestrator

This transition changes the role of the senior manager and the CTO. In the SaaS era, the goal was to select the right tools and ensure the staff was trained to use them. In the Service-as-Software era, the goal is to orchestrate a fleet of autonomous services. The human role shifts from being an operator of software to being an architect of reliable outcomes.

Organizations that cling to the "tool-based" mindset will find themselves burdened with high labor costs and slow execution. The competitive advantage will shift to those who can effectively integrate AI agents into their core business processes, treating them not as additions to the tech stack, but as a scalable, digital workforce. This is the great budget migration: moving from paying for seat licenses and human hours to paying for delivered outcomes [^4].

The software is no longer just helping us do the work. The software is the work.

[^1]: [Thoughtworks: Service-as-software: A new economic model for the age of AI agents](https://www.thoughtworks.com/insights/blog/generative-ai/service-as-software-a-new-economic-model-for-age-of-ai-agents)
[^2]: [Michael Burnett: From SaaS to 'Service-as-Software': How AI Is Repricing the Global Services Economy](https://michaelburnett3.substack.com/p/from-saas-to-service-as-software)
[^3]: [Sequoia Capital: Services: The New Software](https://sequoiacap.com/article/services-the-new-software/)
[^4]: [HFS Research: Ditch same-old SaaS and differentiate with Services-as-Software](https://www.hfsresearch.com/research/saas-services-as-software/)
