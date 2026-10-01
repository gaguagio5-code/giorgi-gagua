frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
backend_skills = {"Python", "JavaScript", "SQL", "React"}

print("Union:", frontend_skills | backend_skills)
print("Intersection:", frontend_skills & backend_skills)
print("Frontend-only:", frontend_skills - backend_skills)
print("Symmetric difference:", frontend_skills ^ backend_skills)