<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Jian Sun · Engineering Mechanics · Fatigue & Fracture</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700&family=Merriweather:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet" />
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" />
    <style>
        /* ----- Reset & Base ----- */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background-color: #f9fafc;
            color: #1e293b;
            line-height: 1.7;
            padding: 2rem 1rem;
        }
        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            padding: 2.5rem 3rem;
            border-radius: 16px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.04);
        }
        /* ----- Typography ----- */
        h1, h2, h3, h4 {
            font-family: 'Merriweather', 'Georgia', serif;
            font-weight: 700;
            letter-spacing: -0.02em;
        }
        h1 {
            font-size: 2.8rem;
            line-height: 1.2;
            color: #0f2b4b;
            margin-bottom: 0.2rem;
        }
        h2 {
            font-size: 1.8rem;
            color: #0f2b4b;
            border-bottom: 3px solid #dce5f0;
            padding-bottom: 0.4rem;
            margin: 2.8rem 0 1.2rem 0;
        }
        h3 {
            font-size: 1.2rem;
            font-weight: 600;
            color: #1e3a5f;
            margin: 1.5rem 0 0.3rem 0;
        }
        .subhead {
            font-size: 1.2rem;
            font-weight: 400;
            color: #2c5282;
            margin-bottom: 1rem;
        }
        a {
            color: #1a56db;
            text-decoration: none;
            transition: color 0.15s;
        }
        a:hover {
            color: #0f3a8a;
            text-decoration: underline;
        }
        /* ----- Header / Bio ----- */
        .header-top {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1.2rem;
        }
        .header-left {
            flex: 1;
        }
        .header-right {
            display: flex;
            gap: 1.2rem;
            font-size: 1.1rem;
            margin-top: 0.6rem;
            flex-wrap: wrap;
        }
        .header-right a {
            color: #1e293b;
            transition: color 0.2s;
        }
        .header-right a:hover {
            color: #1a56db;
            text-decoration: none;
        }
        .bio {
            font-size: 1.05rem;
            margin: 1.5rem 0 0.8rem 0;
            color: #1e293b;
            max-width: 85%;
        }
        /* ----- Research Interests (tags) ----- */
        .interests {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem 1.2rem;
            margin: 1.2rem 0 0.5rem 0;
            padding: 0;
            list-style: none;
        }
        .interests li {
            background: #eef4ff;
            padding: 0.2rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: 500;
            color: #1a3a6b;
        }
        /* ----- Research Statement ----- */
        .research-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            margin: 1rem 0;
        }
        .research-grid .card {
            background: #f8faff;
            padding: 1.2rem 1.5rem;
            border-radius: 12px;
            border-left: 4px solid #1a56db;
        }
        .research-grid .card strong {
            color: #0f2b4b;
        }
        /* ----- Publications ----- */
        .pub-item {
            margin-bottom: 1.5rem;
            padding-bottom: 1.2rem;
            border-bottom: 1px solid #e9edf4;
        }
        .pub-item:last-child {
            border-bottom: none;
        }
        .pub-title {
            font-weight: 600;
            font-size: 1.05rem;
            color: #0a2540;
        }
        .pub-venue {
            font-style: italic;
            color: #3b5a7a;
        }
        .pub-doi {
            font-size: 0.9rem;
            color: #1a56db;
        }
        .pub-note {
            background: #f2f6fc;
            padding: 0.5rem 1rem;
            margin-top: 0.5rem;
            border-radius: 8px;
            font-size: 0.95rem;
            color: #1e3a5f;
            border-left: 3px solid #3b82f6;
        }
        .pub-note i {
            margin-right: 0.3rem;
            color: #1a56db;
        }
        /* ----- Experience / Education ----- */
        .exp-item, .edu-item {
            margin-bottom: 1.2rem;
        }
        .exp-item .title, .edu-item .title {
            font-weight: 600;
            font-size: 1.05rem;
        }
        .exp-item .org, .edu-item .org {
            font-weight: 500;
            color: #1e3a5f;
        }
        .exp-item .date, .edu-item .date {
            color: #64748b;
            font-size: 0.9rem;
            margin-left: 0.5rem;
        }
        .exp-item ul, .edu-item ul {
            margin: 0.3rem 0 0.5rem 1.2rem;
            list-style: disc;
        }
        .exp-item ul li, .edu-item ul li {
            margin-bottom: 0.3rem;
        }
        .skills-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1.5rem;
            margin: 0.5rem 0;
        }
        .skills-grid ul {
            list-style: none;
            padding: 0;
        }
        .skills-grid ul li {
            padding: 0.2rem 0;
            border-bottom: 1px solid #f1f4f9;
        }
        .skills-grid ul li strong {
            display: inline-block;
            min-width: 90px;
            color: #1e3a5f;
        }
        /* ----- Contact / Footer ----- */
        .contact-links {
            display: flex;
            flex-wrap: wrap;
            gap: 1.5rem 2.5rem;
            margin: 1rem 0 0.5rem 0;
            font-size: 1.05rem;
        }
        .contact-links a {
            color: #1e293b;
        }
        .contact-links a i {
            margin-right: 0.4rem;
            color: #1a56db;
            width: 1.4rem;
        }
        .footer-note {
            margin-top: 2.5rem;
            padding-top: 1.5rem;
            border-top: 1px solid #e2e8f0;
            font-size: 0.9rem;
            color: #64748b;
            text-align: center;
        }
        /* ----- Responsive ----- */
        @media (max-width: 768px) {
            .container { padding: 1.5rem; }
            h1 { font-size: 2.2rem; }
            .header-top { flex-direction: column; }
            .header-right { margin-top: 0.6rem; }
            .bio { max-width: 100%; }
            .research-grid { grid-template-columns: 1fr; }
            .skills-grid { grid-template-columns: 1fr; }
        }
        @media (max-width: 480px) {
            .container { padding: 1rem; }
            h1 { font-size: 1.8rem; }
            .contact-links { flex-direction: column; gap: 0.5rem; }
        }
        html { scroll-behavior: smooth; }
        .nav-dots {
            display: flex;
            flex-wrap: wrap;
            gap: 0.8rem 1.8rem;
            margin: 1.2rem 0 0.5rem 0;
            padding: 0.6rem 0;
            border-top: 1px solid #e9edf4;
            border-bottom: 1px solid #e9edf4;
        }
        .nav-dots a {
            font-weight: 500;
            color: #1e3a5f;
            font-size: 0.95rem;
        }
        .nav-dots a:hover {
            color: #1a56db;
            text-decoration: none;
        }
        .badge {
            background: #0f2b4b;
            color: white;
            font-size: 0.7rem;
            padding: 0.1rem 0.6rem;
            border-radius: 12px;
            margin-left: 0.4rem;
            font-weight: 400;
        }
        .placeholder-highlight {
            background: #fef9c3;
            padding: 0.1rem 0.4rem;
            border-radius: 4px;
            color: #854d0e;
        }
    </style>
</head>
<body>

<div class="container">

    <!-- ============================================================ -->
    <!-- HEADER                                                         -->
    <!-- ============================================================ -->
    <header>
        <div class="header-top">
            <div class="header-left">
                <h1>Jian Sun</h1>
                <div class="subhead">Engineering Mechanics · Fatigue &amp; Fracture</div>
            </div>
            <div class="header-right">
                <a href="mailto:sunjian201@mails.ucas.ac.cn"><i class="fas fa-envelope"></i> Email</a>
                <a href="#" target="_blank"><i class="fab fa-google-scholar"></i> Scholar</a>
                <a href="#" target="_blank"><i class="fab fa-linkedin-in"></i> LinkedIn</a>
                <a href="#" target="_blank"><i class="fab fa-orcid"></i> ORCID</a>
            </div>
        </div>

        <!-- quick nav -->
        <div class="nav-dots">
            <a href="#bio">About</a>
            <a href="#interests">Interests</a>
            <a href="#research">Research</a>
            <a href="#publications">Publications</a>
            <a href="#experience">Experience</a>
            <a href="#education">Education</a>
            <a href="#skills">Skills</a>
            <a href="#contact">Contact</a>
        </div>

        <!-- Bio -->
        <div id="bio" class="bio">
            <p>
                I am an engineering mechanics researcher with a Master's degree from the
                <strong>University of Chinese Academy of Sciences</strong>, where I investigated
                fatigue and fracture behaviors of titanium alloys and high-strength steels used
                in critical engineering applications—from aero-engine compressor blades to
                deep-sea submersible pressure hulls. My research integrates experimental
                characterization (SEM/EBSD), numerical modeling (ABAQUS), and statistical
                analysis to understand how defects, notches, and service conditions influence
                crack initiation and early growth in high-cycle and very-high-cycle fatigue regimes.
            </p>
            <p style="margin-top:0.6rem;">
                My work has been published in <em>Engineering Fracture Mechanics</em>,
                <em>International Journal of Fatigue</em>, and <em>Journal of Marine Science and Engineering</em>.
                I am seeking a Ph.D. position to advance the science of structural integrity
                and fatigue mechanics.
            </p>
        </div>
    </header>

    <!-- ============================================================ -->
    <!-- RESEARCH INTERESTS                                             -->
    <!-- ============================================================ -->
    <section id="interests">
        <h2>Research Interests</h2>
        <ul class="interests">
            <li>High-Cycle &amp; Very-High-Cycle Fatigue</li>
            <li>Dwell Fatigue &amp; Time-Dependent Deformation</li>
            <li>Microstructure-Sensitive Fatigue (EBSD)</li>
            <li>Defect &amp; Notch Effects</li>
            <li>Computational Mechanics (ABAQUS, MATLAB)</li>
        </ul>
    </section>

    <!-- ============================================================ -->
    <!-- RESEARCH STATEMENT                                            -->
    <!-- ============================================================ -->
    <section id="research">
        <h2>Research Statement</h2>
        <p style="margin-bottom:0.8rem;">
            My research focuses on multi-scale mechanisms governing fatigue failure in
            titanium alloys and high-strength steels under complex service conditions.
            I combine experimental characterization, in-situ observation, and finite
            element modeling to understand how defects, notches, and time-dependent
            loading alter crack initiation and early growth.
        </p>

        <div class="research-grid">
            <div class="card">
                <strong>📘 Thread 1 · Defect-induced VHCF (TC17)</strong>
                <p style="margin-top:0.3rem;font-size:0.98rem;">
                    Showed that artificial surface defects in TC17 induce rapid failure
                    driven by cyclic stress–environment synergy, explaining the plateau
                    in S–N data and the absence of FGA/RA features.
                </p>
            </div>
            <div class="card">
                <strong>📘 Thread 2 · Dwell fatigue &amp; notches (Ti-6Al-4V ELI)</strong>
                <p style="margin-top:0.3rem;font-size:0.98rem;">
                    Demonstrated dwell fatigue is insensitive to defect size (190–438 μm)
                    and that notched specimens exhibit <em>higher</em> dwell life than
                    smooth specimens at the same local stress—critical for marine design.
                </p>
            </div>
            <div class="card">
                <strong>📘 Thread 3 · Microstructural evolution (quasi in-situ EBSD)</strong>
                <p style="margin-top:0.3rem;font-size:0.98rem;">
                    Captured direct evidence that twinning occurs in α-grains with
                    prismatic SF ≤ 0.2 and dwell stress can both promote <em>and</em>
                    restrain crack growth depending on dwell time.
                </p>
            </div>
            <div class="card">
                <strong>📘 Thread 4 · Aging &amp; discontinuous loading (steels)</strong>
                <p style="margin-top:0.3rem;font-size:0.98rem;">
                    Quantified that natural aging &gt;20,000 h reduces HCF life in
                    25CrMo4 and 30CrMnSiA via corrosion/hydrogen, while discontinuous
                    loading has no harmful effect.
                </p>
            </div>
        </div>

        <h3 style="margin-top:1.2rem;">Key Contributions</h3>
        <ul style="margin-left:1.2rem;">
            <li>Proposed a mechanistic framework for surface-defect-induced VHCF, revealing that crack growth consumes <strong>&lt;20,000 cycles</strong> after initiation.</li>
            <li>Identified that dwell fatigue life in notched Ti-6Al-4V ELI is <strong>higher</strong> than smooth specimens at the same local stress—with no dwell effect on cumulative strain.</li>
            <li>Established that twinning occurs in α-grains with prismatic Schmid factor <strong>≤ 0.2</strong> and c-axis angle <strong>≤ 46°</strong>—irrespective of loading type.</li>
            <li>Quantified that natural aging promotes multi-site crack initiation in 25CrMo4 but does not change the dominant failure mode in 30CrMnSiA.</li>
        </ul>
    </section>

    <!-- ============================================================ -->
    <!-- PUBLICATIONS                                                  -->
    <!-- ============================================================ -->
    <section id="publications">
        <h2>Selected Publications</h2>

        <!-- Pub 1 -->
        <div class="pub-item">
            <div class="pub-title">
                Mechanism of artificial surface defect induced cracking for very high cycle fatigue of Ti alloys
            </div>
            <div class="pub-venue">
                <strong>Sun, J.</strong>, Peng, W., &amp; Sun, C. (2022).
                <em>Engineering Fracture Mechanics</em>, 272, 108721.
                <a href="https://doi.org/10.1016/j.engfracmech.2022.108721" target="_blank" class="pub-doi"> DOI: 10.1016/j.engfracmech.2022.108721</a>
            </div>
            <div class="pub-note">
                <i class="fas fa-bullseye"></i> <strong>Impact:</strong> First direct evidence that VHCF from surface defects is not a purely cyclic process—crack growth consumes &lt;20,000 cycles, challenging conventional life-prediction models.
            </div>
        </div>

        <!-- Pub 2 -->
        <div class="pub-item">
            <div class="pub-title">
                Effects of Notches and Defects on Dwell Fatigue Mechanism and Fatigue Life of Ti-6Al-4V ELI Alloy Used in Deep-Sea Submersibles
            </div>
            <div class="pub-venue">
                <strong>Sun, J.</strong>, Wu, L., &amp; Sun, C. (2021).
                <em>Journal of Marine Science and Engineering</em>, 9(8), 845.
                <a href="https://doi.org/10.3390/jmse9080845" target="_blank" class="pub-doi"> DOI: 10.3390/jmse9080845</a>
            </div>
            <div class="pub-note">
                <i class="fas fa-bullseye"></i> <strong>Impact:</strong> Established that dwell fatigue in notched specimens is insensitive to defect size and that notched specimens exhibit <em>higher</em> dwell fatigue life than smooth specimens at the same local stress—key for pressure hull design.
            </div>
        </div>

        <!-- Pub 3 -->
        <div class="pub-item">
            <div class="pub-title">
                A method of quasi in-situ EBSD observation for microstructure and damage evolution in fatigue and dwell fatigue of Ti alloys
            </div>
            <div class="pub-venue">
                Sun, C., <strong>Sun, J.</strong>, Chi, W., Wang, J., &amp; Wang, W. (2023).
                <em>International Journal of Fatigue</em>, 176, 107897.
                <a href="https://doi.org/10.1016/j.ijfatigue.2023.107897" target="_blank" class="pub-doi"> DOI: 10.1016/j.ijfatigue.2023.107897</a>
            </div>
            <div class="pub-note">
                <i class="fas fa-bullseye"></i> <strong>Impact:</strong> Introduced a novel quasi in-situ EBSD methodology that captures the <em>evolution</em> of twinning and slip during fatigue—revealing that twinning occurs in grains with prismatic SF ≤ 0.2 and that dwell stress can both promote and restrain crack growth.
            </div>
        </div>

        <!-- Pub 4 -->
        <div class="pub-item">
            <div class="pub-title">
                Effects of Natural Aging and Discontinuous Cyclic Loading on High Cycle Fatigue Behavior of Steels
            </div>
            <div class="pub-venue">
                Li, G., Liu, J., <strong>Sun, J.</strong>, &amp; Sun, C. (2023).
                <em>Metals</em>, 13(3), 511.
                <a href="https://doi.org/10.3390/met13030511" target="_blank" class="pub-doi"> DOI: 10.3390/met13030511</a>
            </div>
            <div class="pub-note">
                <i class="fas fa-bullseye"></i> <strong>Impact:</strong> Quantified that long-term natural aging (>20,000 h) reduces HCF life via surface corrosion, not microstructural change, and that discontinuous loading has no harmful effect on fatigue life.
            </div>
        </div>
    </section>

    <!-- ============================================================ -->
    <!-- EXPERIENCE                                                    -->
    <!-- ============================================================ -->
    <section id="experience">
        <h2>Experience</h2>

        <div class="exp-item">
            <div class="title">
                Research Assistant
                <span class="org">· Institute of Mechanics, Chinese Academy of Sciences</span>
                <span class="date">(2020 – 2023)</span>
            </div>
            <ul>
                <li>Investigated VHCF mechanisms in TC17 titanium alloy with artificial surface defects, revealing that crack initiation is driven by cyclic stress–environment synergy and consumes &lt;20,000 cycles.</li>
                <li>Developed ABAQUS models to compute stress concentration factors and control volumes, and implemented MATLAB-based Weibull algorithms to predict P–S–N curves within ±15% accuracy.</li>
                <li>Designed and executed quasi in-situ EBSD experiments (Oxford/HKL Channel 5) to track microstructural evolution in Ti-6Al-4V ELI, capturing the first direct observation of subgrain formation from twinning under cyclic loading.</li>
                <li>Characterized crack initiation facets and deformation twins, identifying that twinning occurs in α-grains with prismatic SF ≤ 0.2 and c-axis angle ≤ 46°—irrespective of loading type.</li>
                <li>Analyzed effects of natural aging (8,800–34,000 h) and discontinuous loading on HCF of 25CrMo4 and 30CrMnSiA steels, quantifying life reduction and promotion of multi-site crack initiation.</li>
            </ul>
        </div>

        <div class="exp-item">
            <div class="title">
                Undergraduate Research Assistant
                <span class="org">· Lanzhou University of Technology</span>
                <span class="date">(2016 – 2017)</span>
            </div>
            <ul>
                <li>Performed experimental testing and data analysis for mechanics of materials laboratory projects (tensile tests, strain gauge measurement).</li>
                <li>Assisted in finite element modeling (ABAQUS) of structural components, validating results against analytical solutions.</li>
            </ul>
        </div>
    </section>

    <!-- ============================================================ -->
    <!-- EDUCATION                                                     -->
    <!-- ============================================================ -->
    <section id="education">
        <h2>Education</h2>

        <div class="edu-item">
            <div class="title">
                M.S. in Engineering Mechanics
                <span class="org">· University of Chinese Academy of Sciences</span>
                <span class="date">(2020 – 2023)</span>
            </div>
            <ul>
                <li><strong>Thesis:</strong> Investigation of Fatigue Crack Initiation and Early Growth Mechanisms in Titanium Alloys and High-Strength Steels <span class="badge">tentative</span></li>
                <li><strong>Advisor:</strong> Prof. Chengqi Sun</li>
                <li><strong>Relevant Coursework:</strong> Finite Element Methods, Nonlinear FEM, Fracture Mechanics, Numerical Analysis</li>
                <li><strong>GPA:</strong> <span class="placeholder-highlight">[Insert GPA if ≥ 3.5/4.0]</span></li>
            </ul>
        </div>

        <div class="edu-item">
            <div class="title">
                B.S. in Engineering Mechanics
                <span class="org">· Lanzhou University of Technology</span>
                <span class="date">(2013 – 2017)</span>
            </div>
            <ul>
                <li><strong>Relevant Coursework:</strong> Advanced Mathematics, Linear Algebra, Probability &amp; Statistics, Theoretical Mechanics, Mechanics of Materials, Elastic Mechanics</li>
                <li><strong>GPA:</strong> <span class="placeholder-highlight">[Insert GPA if ≥ 3.5/4.0]</span></li>
            </ul>
        </div>
    </section>

    <!-- ============================================================ -->
    <!-- SKILLS                                                        -->
    <!-- ============================================================ -->
    <section id="skills">
        <h2>Skills</h2>
        <div class="skills-grid">
            <div>
                <h4 style="font-family:'Inter',sans-serif;font-weight:600;margin-bottom:0.4rem;">Computational &amp; Software</h4>
                <ul>
                    <li><strong>FEA / Simulation</strong> ABAQUS, Nonlinear FEM</li>
                    <li><strong>Programming</strong> MATLAB (Weibull, data viz)</li>
                    <li><strong>Microscopy</strong> SEM, EBSD (Oxford, Channel 5, MTEX)</li>
                    <li><strong>Document Prep</strong> LaTeX, Overleaf</li>
                    <li><strong>General</strong> OriginLab, Image-Pro Plus, MS Office</li>
                </ul>
            </div>
            <div>
                <h4 style="font-family:'Inter',sans-serif;font-weight:600;margin-bottom:0.4rem;">Analytical &amp; Experimental</h4>
                <ul>
                    <li><strong>Fatigue Testing</strong> HCF, VHCF, Dwell, Rotating bending (50 Hz, R = –1)</li>
                    <li><strong>Failure Analysis</strong> Fractography (SEM), FGA/RA, facet analysis</li>
                    <li><strong>Microstructure</strong> EBSD data processing, Schmid factor, KAM mapping</li>
                    <li><strong>Statistics</strong> Weibull distribution, P–S–N curves, survival probability</li>
                </ul>
            </div>
        </div>
        <div style="margin-top:1rem;">
            <h4 style="font-family:'Inter',sans-serif;font-weight:600;margin-bottom:0.2rem;">Languages</h4>
            <ul style="list-style:none;padding:0;display:flex;gap:2rem;flex-wrap:wrap;">
                <li><strong>Chinese (Mandarin)</strong> · Native</li>
                <li><strong>English</strong> · Professional Working Proficiency <span class="placeholder-highlight">[TOEFL/IELTS score]</span></li>
            </ul>
        </div>
    </section>

    <!-- ============================================================ -->
    <!-- CONTACT                                                       -->
    <!-- ============================================================ -->
    <section id="contact">
        <h2>Contact</h2>
        <div class="contact-links">
            <a href="mailto:sunjian201@mails.ucas.ac.cn"><i class="fas fa-envelope"></i> sunjian201@mails.ucas.ac.cn</a>
            <a href="#" target="_blank"><i class="fab fa-google-scholar"></i> Google Scholar</a>
            <a href="#" target="_blank"><i class="fab fa-linkedin-in"></i> LinkedIn</a>
            <a href="#" target="_blank"><i class="fab fa-orcid"></i> ORCID</a>
            <a href="#" target="_blank"><i class="fab fa-github"></i> GitHub</a>
            <a href="#" target="_blank"><i class="fab fa-researchgate"></i> ResearchGate</a>
        </div>
        <p style="margin-top:1rem;color:#475569;font-size:0.95rem;">
            <i class="fas fa-map-pin" style="margin-right:0.4rem;color:#1a56db;"></i>
            Beijing, China · <em>available for Ph.D. positions starting Fall 2025</em>
        </p>
    </section>

    <!-- ============================================================ -->
    <!-- FOOTER                                                        -->
    <!-- ============================================================ -->
    <div class="footer-note">
        <span style="font-family:'Merriweather',serif;">Jian Sun</span> · 
        Last updated June 2026 · 
        Built with <i class="fas fa-heart" style="color:#1a56db;"></i> for GitHub Pages
    </div>

</div>
<!-- end container -->

</body>
</html>
