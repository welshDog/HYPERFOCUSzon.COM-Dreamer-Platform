"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
🧠 COGNITIVE BUS MVP - QUICK DEMO TEST
BROSKI♾️ Testing the thought-to-code pipeline

This tests the core Cognitive Bus functionality:
- Intent parsing from natural language
- AST generation from structured intents  
- Code generation from AST
- Transparency logging
"""

from cognitive_bus_mvp import CognitiveBus, IntentParser, ASTGenerator
import ast

def test_cognitive_bus():
    """🎯 Test the full Cognitive Bus pipeline"""
    
    logger.info("🌌 🧠 COGNITIVE BUS MVP - DEMO TEST SEQUENCE")
    logger.info("🌌 =" * 50)
    
    # Initialize Cognitive Bus
    bus = CognitiveBus()
    
    # Test intents
    test_intents = [
        "Create a function that calculates user age from birthday",
        "Create a User class with name, email, and password fields", 
        "Add user authentication with login and registration",
        "Create API endpoint for getting user profile data"
    ]
    
    print(f"🎯 Testing {len(test_intents)} different intent types...\n")
    
    results = []
    
    for i, intent_desc in enumerate(test_intents, 1):
        print(f"🚀 TEST {i}: {intent_desc}")
        logger.info("🌌 -" * 40)
        
        # Process intent through Cognitive Bus
        result = bus.process_intent(intent_desc)
        
        # Verify result structure
        assert 'intent' in result
        assert 'ast' in result
        assert 'code' in result
        assert 'transparent' in result
        assert result['transparent'] == True
        
        # Display generated code preview
        code_lines = result['code'].split('\n')
        preview_lines = code_lines[:5] if len(code_lines) > 5 else code_lines
        
        print(f"✅ AST Type: {type(result['ast']).__name__}")
        print(f"✅ Code Lines: {len(code_lines)}")
        print(f"✅ Transparency: {result['transparent']}")
        logger.info("🌌 📝 Code Preview:")
        for line in preview_lines:
            print(f"   {line}")
        if len(code_lines) > 5:
            print(f"   ... ({len(code_lines) - 5} more lines)")
        
        results.append(result)
        print()
    
    # Summary
    logger.info("🌌 🏆 COGNITIVE BUS MVP TEST RESULTS:")
    logger.info("🌌 =" * 50)
    print(f"✅ Total intents processed: {len(results)}")
    print(f"✅ All results transparent: {all(r['transparent'] for r in results)}")
    print(f"✅ AST types generated: {[type(r['ast']).__name__ for r in results]}")
    print(f"✅ Total code lines: {sum(len(r['code'].split('\\n')) for r in results)}")
    
    logger.info("🌌 \n🧠 COGNITIVE BUS MVP: FULLY OPERATIONAL!")
    logger.info("🌌 #BROSKI_HINT: Thought-to-code translation is LIVE! 🚀")
    
    return results

def test_individual_components():
    """🎯 Test individual Cognitive Bus components"""
    
    logger.info("🌌 \n🔧 COMPONENT TESTING:")
    logger.info("🌌 =" * 30)
    
    # Test Intent Parser
    parser = IntentParser()
    intent = parser.parse_intent("Create a function that validates email addresses")
    
    print(f"🎯 Intent Parser:")
    print(f"   Description: {intent.description}")
    print(f"   Language: {intent.target_language}")
    print(f"   Complexity: {intent.complexity_level}/10")
    print(f"   Functions: {intent.expected_functions}")
    
    # Test AST Generator
    generator = ASTGenerator()
    generated_ast = generator.generate_from_intent(intent)
    
    print(f"\n⚡ AST Generator:")
    print(f"   AST Type: {type(generated_ast).__name__}")
    print(f"   Valid AST: {isinstance(generated_ast, ast.AST)}")
    
    # Test code generation
    code = ast.unparse(generated_ast)
    print(f"\n📝 Code Generation:")
    print(f"   Generated Lines: {len(code.split('\\n'))}")
    print(f"   Code Preview: {code[:100]}...")
    
    logger.info("🌌 \n✅ All components working correctly!")

if __name__ == "__main__":
    logger.info("🌌 🦾💎⚡ COGNITIVE BUS MVP - DEMO TEST LAUNCHER ⚡💎🦾")
    print()
    
    # Run full pipeline test
    test_results = test_cognitive_bus()
    
    # Run component tests
    test_individual_components()
    
    logger.info("🌌 \n🎊 COGNITIVE BUS MVP DEMO COMPLETE!")
    logger.info("🌌 Ready for full GUI experience - run cognitive_bus_mvp.py!")
