const caseStudies = {
  case1: {
    kicker: 'Case Study 01 · Data Quality',
    title: 'Validating complex data and reporting logic',
    body: `
      <h3>The challenge</h3>
      <p>A data-driven reporting platform produced outputs based on multiple configuration rules, demographic breakdowns, reporting conditions, and calculated indicators. UI-only validation was not sufficient because a value could look correct while being derived from incorrect logic.</p>
      <h3>My role</h3>
      <ul><li>Review calculation rules and requirements</li><li>Identify risky combinations and edge cases</li><li>Design scenario-based coverage</li><li>Validate backend data with SQL</li><li>Compare expected and actual results</li><li>Execute regression across related dashboards and workflows</li></ul>
      <h3>Approach</h3>
      <p>I broke complex rules into individual conditions, combined them into structured scenarios, and validated expected outputs independently using backend data. This helped isolate configuration-specific defects that would have been difficult to catch through UI testing alone.</p>
      <h3>Outcome</h3>
      <p>Stronger data confidence, clearer defect evidence, and earlier identification of risky reporting logic before release.</p>
      <h3>Skills demonstrated</h3>
      <p>SQL, business-rule testing, scenario modelling, exploratory testing, requirements analysis, regression testing, and technical investigation.</p>`
  },
  case2: {
    kicker: 'Case Study 02 · Automation',
    title: 'Building maintainable web regression automation',
    body: `
      <h3>The challenge</h3>
      <p>As regression suites grow, automation can become slow, brittle, and expensive to maintain. The goal was not to automate everything, but to create reliable coverage around high-value workflows.</p>
      <h3>My role</h3>
      <ul><li>Identify high-value automation candidates</li><li>Design reusable structures and commands</li><li>Develop Cypress-based automated tests</li><li>Manage test data and environment concerns</li><li>Investigate flaky tests</li><li>Support CI/CD execution</li></ul>
      <h3>Approach</h3>
      <p>I prioritised automation according to business risk, execution frequency, stability, and maintenance cost. Repeated behaviours were extracted into reusable helpers so that test suites stayed readable and easier to maintain.</p>
      <h3>Outcome</h3>
      <p>Reduced manual regression effort by up to 50%, shortened testing cycles, and helped teams release faster with more reliable repeatable checks.</p>
      <h3>Skills demonstrated</h3>
      <p>Cypress, JavaScript/TypeScript, regression strategy, reusable test design, Git, CI/CD, and browser debugging.</p>`
  },
  case3: {
    kicker: 'Case Study 03 · Investigation',
    title: 'Tracing defects beyond the user interface',
    body: `
      <h3>The challenge</h3>
      <p>Unexpected application behaviour required determining whether the issue came from frontend rendering, API responses, configuration, business logic, or underlying data.</p>
      <h3>Investigation flow</h3>
      <ul><li>Reproduce the problem consistently</li><li>Change one variable at a time</li><li>Inspect console and network activity in DevTools</li><li>Validate request payloads and API responses</li><li>Compare application behaviour with stored data</li><li>Compare environments where relevant</li><li>Document technical evidence alongside reproduction steps</li></ul>
      <h3>Outcome</h3>
      <p>Providing evidence from multiple layers reduced ambiguity between QA and engineering, helped narrow the investigation to the most likely failure point, and supported a measurable reduction in production defects.</p>
      <h3>Skills demonstrated</h3>
      <p>DevTools, API testing, SQL, root-cause isolation, environment comparison, defect reporting, and exploratory testing.</p>`
  },
  case4: {
    kicker: 'Case Study 04 · Leadership',
    title: 'Leading quality across multiple workstreams',
    body: `
      <h3>The challenge</h3>
      <p>Supporting multiple products or squads at the same time creates competing priorities between new features, reopened defects, regression work, release deadlines, and unplanned support.</p>
      <h3>My role</h3>
      <ul><li>Sprint QA planning and effort estimation</li><li>Risk identification and prioritisation</li><li>Regression planning</li><li>Reopened-defect management</li><li>Release readiness communication</li><li>Stakeholder alignment</li><li>Mentoring and supporting QA colleagues</li></ul>
      <h3>Approach</h3>
      <p>I treat QA planning as risk management. Priorities are influenced by business criticality, technical complexity, scope of change, regression risk, and release timing. During release, I communicate what was tested, what remains untested, known defects, and the residual risk of shipping.</p>
      <h3>Outcome</h3>
      <p>Improved test efficiency by 35%, mentored 9 junior QAs, reduced feedback loops by 25%, and supported predictable delivery across competing workstreams.</p>
      <h3>Skills demonstrated</h3>
      <p>QA leadership, test strategy, sprint planning, risk management, release communication, mentoring, and cross-functional collaboration.</p>`
  }
};

const modal = document.getElementById('caseModal');
const modalContent = document.getElementById('modalContent');
const closeButton = document.querySelector('.modal-close');

document.querySelectorAll('.case-trigger').forEach(button => {
  button.addEventListener('click', () => {
    const data = caseStudies[button.dataset.case];
    modalContent.innerHTML = `<div class="modal-kicker">${data.kicker}</div><h2>${data.title}</h2>${data.body}`;
    modal.showModal();
  });
});

closeButton.addEventListener('click', () => modal.close());
modal.addEventListener('click', event => {
  const rect = modal.getBoundingClientRect();
  const outside = event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom;
  if (outside) modal.close();
});

document.getElementById('year').textContent = new Date().getFullYear();

const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
