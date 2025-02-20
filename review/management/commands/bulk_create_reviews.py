"""
    review/management/commands/bulk_create_reviews.py
    Command to generate and insert bulk product reviews into the database
"""

import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings
from review.models import Review
from user.models import User

LOCAL_IMAGE_FOLDER = r"C:\Users\Raghu Gannaram\Pictures\silicon_valley\products"
MEDIA_FOLDER = os.path.join(settings.MEDIA_ROOT, "reviews")

os.makedirs(MEDIA_FOLDER, exist_ok=True)

USERS_REVIEWS = {
    "richard": [
        (
            "Pied Piper Algorithm",
            "Software",
            "The most efficient lossless compression algorithm ever built! 🚀 Pied Piper's innovation in data compression is truly groundbreaking. With an unprecedented Weissman Score, this technology is poised to revolutionize cloud storage, making data transfer faster and more secure than ever before. A must-have for every developer working with large-scale data systems. This will change how we handle digital information forever.",
            5,
            "compression,software,cloud,data-optimization,innovation",
            "pied-piper-algorithm-by-richard",
            "piedpiperalgorithm.webp",
        ),
        (
            "MacBook Pro M3",
            "Laptops",
            "The M3 MacBook Pro is an absolute powerhouse! 🔋 With its new silicon, it delivers unparalleled speed, efficiency, and battery life. The Retina display is stunning, and the keyboard provides the best typing experience. This laptop handles everything from compiling large projects to running multiple virtual machines without breaking a sweat. Highly recommended for developers and power users who need a reliable and fast machine.",
            4,
            "apple,macbook,m3-chip,laptops,developer-tool",
            "macbook-pro-m3-by-richard",
            "macbook_pro_m3.jpg",
        ),
        (
            "ThinkPad X1 Carbon",
            "Laptops",
            "ThinkPad keyboards are still unmatched in the industry. This ultrabook is light, fast, and powerful enough for any developer. With great battery life, a durable build, and a sleek matte finish, it stands out as one of the most premium business laptops available. I personally love the tactile feel of the keyboard, making long coding sessions enjoyable. It's a must-have for professionals who need reliability without compromising on portability. Absolutely worth the investment.",
            3,
            "laptops,thinkpad,carbon,developer,hardware",
            "thinkpad-x1-carbon-by-richard",
            "thinkpad_x1_carbon.jpg",
        ),
        (
            "JetBrains IntelliJ IDEA",
            "Software",
            "One of the best IDEs for Java development! ⚡ IntelliJ IDEA provides excellent refactoring tools, intelligent code suggestions, and deep integration with version control systems. It speeds up development time with its intuitive UI and smooth debugging experience. I have been using it for years, and it has significantly boosted my productivity. Perfect for large-scale development, and if you're serious about Java, this is the only IDE you should consider.",
            3,
            "intellij,jetbrains,java,ide,software",
            "intellij-idea-by-richard",
            "jetbrains_intellij_idea.png",
        ),
        (
            "Raspberry Pi 4",
            "Hardware",
            "An amazing piece of hardware for IoT and prototyping! 🛠️ The Raspberry Pi 4 is more powerful, energy-efficient, and offers better connectivity than its predecessors. Perfect for students, hobbyists, and developers experimenting with embedded systems. Whether you're building an automated home system or learning to code, this tiny device packs a punch. The new CPU makes running AI models much smoother. Definitely a must-have for any tinkerer!",
            4,
            "raspberry-pi,hardware,iot,prototyping,development",
            "raspberry-pi-4-by-richard",
            "raspberrypi5.webp",
        ),
    ],
    "erlich": [
        (
            "Tesla Model X",
            "Cars",
            "Aviato-worthy electric beast! 🚘 The self-driving capability of Tesla's Model X is the closest thing we have to the future. The falcon-wing doors scream luxury, and the acceleration is simply mind-blowing. The range is fantastic, and the charging network is vast. This car isn't just a vehicle; it's a statement. If you want the best of electric performance with tech-packed features, this is it.",
            5,
            "tesla,electric,ev,self-driving,luxury",
            "tesla-model-x-by-erlich",
            "tesla_model_x.avif",
        ),
        (
            "VR Headset Oculus Quest",
            "Gadgets",
            "Immersive and easy to use. 🎮 The Oculus Quest brings VR gaming to the next level with its wireless capabilities and ultra-responsive tracking. The games are mind-blowing, and the feeling of stepping into a different world is just surreal. Whether it's gaming, workouts, or even virtual meetings, VR is here to stay, and this headset is leading the charge.",
            4,
            "vr,gaming,oculus,virtual-reality,tech",
            "oculus-quest-by-erlich",
            "vr_headset_oculus_quest.jpg",
        ),
        (
            "NFT Art Collection",
            "Digital Assets",
            "I bought an Ape NFT, and it's the future of art! 🖼️ NFTs are revolutionizing the way we think about digital ownership. These digital collectibles are not just images; they represent culture, status, and exclusivity. The blockchain ensures authenticity, making it impossible to forge. If you're not into NFTs yet, you might be missing out on the next big wave of investment.",
            1,
            "nft,crypto,blockchain,digital-art,investment",
            "nft-art-collection-by-erlich",
            "ape_nft_art_collection.webp",
        ),
        (
            "Google Nest Hub",
            "Smart Home",
            "My smart home setup is complete! 🏠 Google Nest Hub makes controlling my house effortless. Voice commands for lights, music, and even security cameras make life much easier. The display is super responsive, and Google Assistant integration is top-notch. If you're building a smart home, this is a must-have centerpiece.",
            1,
            "smart-home,google,automation,voice-control,ai",
            "google-nest-hub-by-erlich",
            "google_nesthub.webp",
        ),
        (
            "Beats Studio Pro",
            "Audio",
            "Bass-heavy but stylish! 🎧 These are perfect for travel, with their active noise cancellation blocking out the world. The battery life is solid, and the sound quality is deep and immersive. The build quality feels premium, and the new spatial audio feature makes movies and music come alive. If you love bass and style, these are for you!",
            4,
            "audio,headphones,noise-cancelling,beats,music",
            "beats-studio-pro-by-erlich",
            "beast_studio_pro.jpg",
        ),
    ],
    "dinesh": [
        (
            "NVIDIA RTX 4090",
            "GPUs",
            "GPUs are my life. This one is insanely powerful for machine learning, deep learning, and high-end gaming! 🔥 With 24GB of VRAM, insane tensor core performance, and real-time ray tracing, this is hands down the most powerful consumer GPU ever created. The AI and rendering capabilities are off the charts, making it an absolute beast for professional workloads. If you're into AI development or want the best gaming experience possible, the RTX 4090 is the ultimate choice.",
            4,
            "gpu,ai,deep-learning,nvidia,ml",
            "nvidia-rtx-4090-by-dinesh",
            "nvdia_rtx_4090.jpg"

        ),
        (
            "Python 3.11",
            "Software",
            "The fastest Python release yet! 🚀 Python 3.11 brings incredible performance improvements, better exception handling, and more efficient memory usage. The speedup in computational workloads is noticeable, making it an even better choice for AI and data science. Typing hints and structural pattern matching are maturing well, and as a Python developer, I can confidently say this version is a must-upgrade. If you're still on an older version, you're missing out!",
            5,
            "python,software,ai,performance,coding",
            "python-3-11-by-dinesh",
            "nvdia_rtx_4090.jpg",
        ),
        (
            "Samsung Galaxy Z Fold 4",
            "Smartphones",
            "Foldables are the future! 📱 The multitasking experience on this device is unmatched. Being able to use three apps side by side is a dream for productivity. The inner display is stunning, and the durability improvements make this a serious contender for daily use. Samsung has truly perfected foldable tech, and if you're someone who loves innovation, this is the best phone you can get right now.",
            4,
            "smartphone,foldable,samsung,multitasking,innovation",
            "samsung-galaxy-z-fold-4-by-dinesh",
            "samsung_galaxy_z_fold_5.avif",
        ),
        (
            "Redragon Mechanical Keyboard",
            "Accessories",
            "Clicky heaven! ⌨️ Once you go mechanical, you never go back. The tactile feedback, customizable switches, and satisfying keystrokes make typing so much more enjoyable. Whether you're a programmer or a gamer, having a mechanical keyboard with custom keycaps enhances the experience. I personally use a hot-swappable board with custom switches, and it's by far the best investment for productivity.",
            5,
            "keyboard,mechanical,custom,programming,accessories",
            "mechanical-keyboard-by-dinesh",
            "redragon_mechanical_keyboard.webp",
        ),
        (
            "AirPods Pro 2",
            "Audio",
            "The best noise cancellation on the market! 🎧 The transparency mode is surprisingly natural, and the adaptive audio makes listening seamless. The sound quality has been greatly improved, and the new H2 chip provides ultra-low latency. For workouts, travel, or just zoning out, these are my go-to earbuds. Battery life is solid, and the new case with a speaker and precision finding is a great touch.",
            4,
            "audio,earbuds,noise-cancelling,apple,wireless",
            "airpods-pro-2-by-dinesh",
            "airpods_pro_2.jpg",
        ),
    ],
    "gilfoyle": [
        (
            "Bitcoin Ledger Nano X",
            "Cryptocurrency",
            "The only way to securely store your Bitcoin. 🔒 If you leave your crypto on an exchange, you're gambling with your assets. With cold storage, two-factor authentication, and multi-signature support, this ensures your funds remain truly decentralized. I wouldn't trust any centralized exchange; self-custody is key. If you own crypto and care about security, a hardware wallet like this is non-negotiable. HODL and protect your wealth the right way.",
            4,
            "cryptocurrency,bitcoin,security,ledger,hardware-wallet",
            "bitcoin-ledger-nano-x-by-gilfoyle",
            "bitcoin_ledger_nano_x.webp",
        ),
        (
            "Linux Arch",
            "Operating Systems",
            "Real developers use Arch. 🏴‍☠️ It's not for the weak. If you're still using Windows or macOS, you're basically a sheep. Arch is lightweight, customizable, and gives you full control over your system without the unnecessary bloat. Yes, it has a steep learning curve, but once you master it, you'll never go back to mainstream operating systems. Rolling updates, maximum security, and zero nonsense—this is the OS of true power users.",
            3,
            "linux,operating-systems,arch,security,developers",
            "linux-arch-by-gilfoyle",
            "linux_arch.jpg",
        ),
        (
            "Dark Web VPN",
            "Security",
            "Privacy matters. 🔥 A VPN that provides complete anonymity and strong encryption is essential in today's world of constant surveillance. Whether you're a cybersecurity enthusiast, a journalist, or just someone who values their digital freedom, a no-log VPN is a must-have. With features like multi-hop routing, Tor integration, and AES-256 encryption, this VPN makes tracking you nearly impossible. Stay secure, stay anonymous, and most importantly—stay off the grid.",
            4,
            "vpn,privacy,security,encryption,dark-web",
            "dark-web-vpn-by-gilfoyle",
            "darkweb_vpn.webp",
        ),
        (
            "Ethereum 2.0",
            "Cryptocurrency",
            "Proof-of-Stake is finally here! 🔥 Ethereum 2.0 introduces staking, faster transactions, and reduced fees while making the blockchain more eco-friendly. For years, Ethereum was criticized for high gas fees, but now with this upgrade, transactions are more efficient than ever. Staking rewards are an added bonus for long-term holders, and the security enhancements ensure decentralization remains intact. This is the future of smart contracts and Web3, and I'm here for it.",
            4,
            "ethereum,crypto,blockchain,staking,web3",
            "ethereum-2-by-gilfoyle",
            "ethereun_2_0.webp",
        ),
        (
            "Synology NAS",
            "Storage",
            "Cloud storage? No thanks. 🚀 Storing data on Big Tech servers is a disaster waiting to happen. With a Synology NAS, I have full control over my backups, media, and private files without worrying about being spied on. It's fast, scalable, and reliable, with RAID support to prevent data loss. If you truly value your privacy, stop using Google Drive and Dropbox, and set up a NAS instead. Your data belongs to you, not some corporation.",
            2,
            "storage,nas,privacy,backup,self-hosted",
            "synology-nas-by-gilfoyle",
            "synology_nas.png",
        ),
    ],
    "jared": [
        (
            "Notion App",
            "Productivity",
            "The best note-taking and organization app! 📒 I use Notion to plan every aspect of my life—daily tasks, long-term goals, and project management. It's intuitive, beautifully designed, and customizable for different workflows. Whether you're a student, professional, or entrepreneur, this is the ultimate productivity tool. I honestly can't function without it anymore!",
            4,
            "productivity,organization,notion,task-management,note-taking",
            "notion-app-by-jared",
            "notion_app.png",
        ),
        (
            "Pomodoro Timer",
            "Productivity",
            "Focused work sessions equal maximum efficiency! The Pomodoro technique has changed my workflow completely. The structured 25-minute work sprints followed by short breaks keep my mind sharp and prevent burnout. If you struggle with procrastination or distractions, this is an absolute lifesaver. Highly recommended for anyone who values deep work and time management.",
            4,
            "productivity,time-management,focus,work-efficiency,pomodoro",
            "pomodoro-timer-by-jared",
            "pomodoro_timer.jpg",
        ),
        (
            "Standing Desk",
            "Office",
            "Health first! Working while standing up is a game-changer. 💪 Sitting for long hours is terrible for your posture and energy levels. Ever since I switched to a standing desk, I've felt more active, engaged, and focused throughout the day. It reduces back pain and keeps me moving. If you're working long hours, this investment is 100% worth it.",
            3,
            "office,health,productivity,ergonomics,standing-desk",
            "standing-desk-by-jared",
            "standing_desk.webp",
        ),
        (
            "Noise Cancelling Headphones",
            "Audio",
            "Block distractions. Focus mode enabled! 🎧 The noise cancellation on these headphones is absolutely phenomenal. Whether I'm working in a busy café or need to focus in a noisy office, they create a silent bubble of productivity. Comfortable to wear for hours, with crystal-clear audio. Once you start using them, you'll wonder how you ever worked without them!",
            4,
            "audio,noise-cancellation,productivity,focus,headphones",
            "noise-cancelling-headphones-by-jared",
            "noise_cancelling_headphones.jpg",
        ),
        (
            "Tesla Solar Panels",
            "Energy",
            "Sustainable living is the future! 🌱 I firmly believe in energy efficiency, and Tesla's solar panels are a fantastic investment. They help reduce carbon footprint while significantly lowering electricity bills. Paired with a Powerwall, you can practically go off-grid and have uninterrupted energy. The future of clean energy starts here!",
            1,
            "energy,sustainability,solar,eco-friendly,tesla",
            "tesla-solar-panels-by-jared",
            "tesla_solar_panels.jpg",
        ),
    ],
    "gavin": [
        (
            "Hooli AI Cloud",
            "Software",
            "The most powerful AI infrastructure in the world! 🤖 Hooli is revolutionizing enterprise AI solutions with cutting-edge deep learning models and cloud-based intelligence. Our cloud services offer unmatched scalability, security, and efficiency, enabling businesses to automate their workflows and gain data-driven insights faster than ever. Companies that integrate Hooli AI into their operations experience exponential productivity and cost savings. The future belongs to those who embrace AI, and Hooli leads the way.",
            4,
            "ai,cloud-computing,hooli,enterprise,automation",
            "hooli-ai-cloud-by-gavin",
            "hooli_ai_cloud.jpg",
        ),
        (
            "Mac Pro M2 Ultra",
            "Hardware",
            "Innovation at its peak. Absolute beast of a machine! 🚀 The Mac Pro M2 Ultra is a powerhouse designed for professionals working with AI, film production, and enterprise computing. Its raw processing power, optimized cooling system, and cutting-edge architecture make it the ultimate workstation for high-performance workloads. If you're serious about speed and reliability in your work, this is the machine to own. Hooli developers swear by it, and so should you.",
            4,
            "mac-pro,hardware,performance,ai-training,film-editing",
            "mac-pro-m2-ultra-by-gavin",
            "mac_pro_m2_ultra.jpg",
        ),
        (
            "Quantum Computing Lab",
            "Technology",
            "The future is quantum, and Hooli is leading the charge. 🚀 Quantum computing will redefine computational power, making today's supercomputers look like ancient relics. By investing in quantum technology, Hooli is ensuring that we stay ahead in the trillion-dollar industry of next-gen computing. From cryptography to complex simulations, quantum will unlock possibilities beyond imagination. If you're not thinking quantum, you're already obsolete.",
            3,
            "quantum-computing,hooli,future-tech,supercomputers,innovation",
            "quantum-computing-lab-by-gavin",
            "quantum_computing_lab.jpg",
        ),
        (
            "Hooli AI Assistant",
            "AI",
            "AI is the future, and Hooli AI Assistant is the most advanced virtual assistant ever built. 🤖 This isn't just voice commands—it understands human intent, automates workflows,analyzes emotions, and adapts to business needs in real time. Employees will become obsolete as Hooli AI seamlessly takes over repetitive tasks, making enterprises more efficient than ever. Welcome to the future of work, powered by AI.",
            4,
            "ai,automation,hooli,virtual-assistant,business-tech",
            "hooli-ai-assistant-by-gavin",
            "hooli_ai_cloud.jpg",
        ),
        (
            "5G Private Network",
            "Telecom",
            "Fast, secure, and reliable—exactly what enterprises need. Hooli's 5G private network is tailored for businesses that demand high-speed, low-latency connectivity. No more congestion from public networks, no security risks, just pure, uninterrupted bandwidth. With the rise of remote work and AI-powered analytics, having a private 5G network will soon be the gold standard for modern enterprises.",
            4,
            "5g,network,enterprise,hooli,telecom",
            "5g-private-network-by-gavin",
            "5g_network.jpg",
        ),
    ],
    "russ": [
        (
            "Lamborghini Huracán",
            "Cars",
            "Fast. Loud. Expensive. Exactly how I like it! 🔥 Nothing compares to the roar of a V10 engine at full speed. The handling is razor-sharp, making every corner feel like a racetrack. The carbon fiber body, aerodynamic design, and luxurious interior make it the ultimate status symbol. If you want to turn heads and own the road, this is the car for you.",
            2,
            "luxury,supercar,lamborghini,v10,fast-cars",
            "lamborghini-huracan-by-russ",
            "lamborghini_huracan.avif",
        ),
        (
            "Whiskey Collector's Edition",
            "Drinks",
            "Aged 50 years, smooth, and costs a fortune. This is not just whiskey; it's an investment. 🥃 Every sip is a taste of history, with rich flavors of oak, caramel, and a hint of smokiness. Only real billionaires understand the value of fine-aged spirits. When you drink this, you're not just having whiskey - you're experiencing pure craftsmanship and tradition.",
            3,
            "whiskey,collector-edition,aged-spirits,luxury-drinks",
            "whiskey-collectors-edition-by-russ",
            "whiskey_collecters_edition.jpg",
        ),
        (
            "Private Jet",
            "Luxury",
            "Travel like a billionaire, because I am one. 🛩️ Flying commercial is for peasants. A private jet means total freedom—no waiting in lines, no security checks, and absolute privacy. The in-flight champagne, custom leather seats, and personal crew make every trip a five-star experience. If you're serious about luxury, you need a jet. Period.",
            4,
            "luxury,private-jet,travel,elite-lifestyle",
            "private-jet-by-russ",
            "private_jet.jpg",
        ),
        (
            "Gold Apple Watch",
            "Wearables",
            "Nothing screams wealth more than a gold Apple Watch. ⌚💰 It's a masterpiece of technology and style, blending high-end materials with top-tier smartwatch features. The gold finish makes sure people know you're successful before you even say a word. This is not just a gadget; it's a statement. If you don't have one, you're already behind.",
            1,
            "apple-watch,gold,wearables,luxury-tech,smartwatch",
            "gold-apple-watch-by-russ",
            "gold_apple_watch.jpg",
        ),
        (
            "Bitcoin Mining Rig",
            "Crypto",
            "Gotta keep stacking sats. 🚀 This custom-built mining rig runs 24/7, pulling in Bitcoin like a digital gold rush. With high-powered GPUs and advanced cooling systems, it's an absolute beast. Proof-of-work is king, and if you're not mining, you're missing out on the future of decentralized finance. Passive income at its finest!",
            4,
            "crypto,bitcoin,mining-rig,passive-income,blockchain",
            "bitcoin-mining-rig-by-russ",
            "bhitcoin_minnig_rig.jpg",
        ),
    ],
    "monica": [
        # (
        #     "Investment Portfolio Manager",
        #     "Finance",
        #     "A must-have tool for every investor. This platform allows you to track your stocks, bonds, and crypto investments in real time. The advanced analytics and intuitive UI make it incredibly easy to manage diversified portfolios. Highly recommended for both beginners and experienced traders looking to optimize their investments.",
        #     4,
        #     "finance,investment,portfolio-management,analytics,wealth",
        #     "investment-portfolio-manager-by-monica",
        # ),
        (
            "Tesla Model Y",
            "Cars",
            "Sustainable and efficient. Love the minimal design! The smooth acceleration and autopilot features make it one of the best electric cars in the market. Tesla's ecosystem, from supercharging to software updates, is miles ahead of competitors. If you're looking for an EV with range and tech, this is it.",
            4,
            "electric-car,tesla,autopilot,sustainability,ev",
            "tesla-model-y-by-monica",
            "tesla_model_y.jpg",
        ),
        (
            "MacBook Air M2",
            "Laptops",
            "Light, powerful, and the best for mobility. The M2 chip provides incredible performance without sacrificing battery life. The fanless design keeps it silent, and the Retina display is crystal clear. Whether you're an investor analyzing charts or a student taking notes, this laptop is a game-changer!",
            3,
            "laptop,apple,macbook,m2-chip,ultraportable",
            "macbook-air-m2-by-monica",
            "macbook_air_m2.jpg",
        ),
        (
            "Noise Canceling Earbuds",
            "Audio",
            "Great for focusing in a noisy office! The active noise cancellation is top-tier, allowing me to concentrate on deep work without distractions. The audio quality is crisp, with deep bass and balanced mids. Perfect for travel, work, and workouts. Once you try these, there's no going back!",
            1,
            "audio,noise-cancelling,earbuds,productivity,music",
            "noise-canceling-earbuds-by-monica",
            "noise_cancelling_earbuds.webp",
        ),
        (
            "AI Stock Prediction Tool",
            "Books",
            "Predictive AI at its finest! This tool uses machine learning to analyze historical stock data and provide investment insights. While no AI is 100% accurate, this one offers impressive trend predictions. A great tool for investors looking to get an edge in the market!",
            4,
            "ai,finance,stock-market,investment,trend-prediction",
            "ai-stock-prediction-tool-by-monica",
            "ai_stock_prediction_tool.jpg",
        ),
    ],
    "laurie": [
        (
            "Warren Buffett's Investment Strategy",
            "Books",
            "A masterpiece on long-term investing. 📈 This book dives deep into the investment philosophies of one of the greatest investors of all time. It emphasizes the importance of patience, fundamental analysis, and understanding businesses rather than just stock prices. For investors seeking sustainable growth rather than short-term gains, this is a must-read. Clear insights, real-world examples, and sound financial advice make this an invaluable resource!",
            4,
            "finance,investing,long-term-strategy,warren-buffett,stocks",
            "warren-buffett-investment-strategy-by-laurie",
            "warren_buffett_investment_principles.jpg",
        ),
        (
            "Tesla Powerwall",
            "Energy",
            "A revolution in home energy storage. ⚡ Sustainable energy solutions like the Tesla Powerwall are the future. It enables homeowners to store solar energy and reduce dependence on the grid, cutting electricity costs significantly. As an investor in innovative technology, I see this as a game-changer for the energy sector.  The efficiency and scalability of Tesla's energy solutions are impressive, making them a great choice for anyone looking to embrace renewable energy!",
            4,
            "sustainability,energy,renewables,tesla,battery-storage",
            "tesla-powerwall-by-laurie",
            "tesla_powerwall.avif",
        ),
        (
            "Bloomberg Terminal",
            "Books",
            "The ultimate tool for financial professionals. 🖥️ Bloomberg Terminal provides real-time financial data, analytics, and market intelligence that every serious investor needs. It's expensive, but if you're managing large assets, the insights it delivers are worth every penny. The real-time tracking, global economic data, and AI-powered financial analysis make decision-making incredibly efficient. A must-have for hedge fund managers, analysts, and investment firms!",
            4,
            "finance,stocks,investing,analytics,business",
            "bloomberg-terminal-by-laurie",
            "the_bloom_berg_terminal_beginner_guide.jpg",
        ),
        (
            "Apple Watch Ultra",
            "Wearables",
            "A premium smartwatch for professionals. ⌚ The Apple Watch Ultra is designed for durability, productivity, and high-performance tracking. With advanced health features, GPS tracking, and long battery life, it's the perfect companion for executives and investors who need to stay connected. Its rugged design makes it ideal for those with active lifestyles, and the seamless integration with Apple's ecosystem is a huge plus. A great tool for efficiency and daily productivity!",
            1,
            "apple,wearables,smartwatch,productivity,fitness",
            "apple-watch-ultra-by-laurie",
            "apple_watch_ultra.webp",
        ),
        (
            "The Economist Subscription",
            "Business",
            "Essential reading for staying ahead in global markets. 🌍 The Economist provides in-depth analysis of financial markets, business trends, and political affairs that directly impact the economy. For investors and business leaders, staying informed is non-negotiable, and this publication is a key resource. The coverage is balanced, insightful, and data-driven, making it an invaluable tool for professionals navigating complex economic landscapes.",
            4,
            "business,economy,finance,news,investment",
            "the-economist-subscription-by-laurie",
            "the-echonomist_subscription.jpg",
        ),
    ],
    "bighead": [
        (
            "YouTube Premium",
            "Streaming",
            "No ads, pure entertainment. Worth every penny. I can't imagine going back to watching unskippable ads. This service is absolutely worth the money, and the background play feature is a lifesaver. Highly recommend it!",
            3,
            "ad-free,video-streaming,music,subscription,entertainment",
            "youtube-premium-by-bighead",
            "youtube_premium.png",
        ),
        (
            "Hooli Box",
            "Gadgets",
            "Not sure what this does exactly, but it looks pretty futuristic. I mean, if it's from Hooli, it must be cool, right? Maybe one day I'll figure out all the features it has. But until then, it sits on my desk looking high-tech.",
            5,
            "hooli,smart-home,automation,gadget,ai",
            "hooli-box-by-bighead",
            "hooli_box.jpg",
        ),
        (
            "Apple Vision Pro",
            "Wearables",
            "This is the future of computing! 🥽 The immersive experience is absolutely mind-blowing. It feels like you're inside a sci-fi movie. The interface is intuitive, and the potential applications are endless. Can't wait to see how this evolves!",
            4,
            "augmented-reality,vr,apple,innovation,futuristic",
            "apple-vision-pro-by-bighead",
            "apple_vision_pro.png",
        ),
        (
            "Oculus VR Gloves",
            "Gaming",
            "The future of gaming is here. The haptic feedback in these gloves makes VR gaming way more immersive than ever before. It's still early tech, but I'm excited to see where this goes. The potential is insane! 🎮",
            1,
            "vr,gaming,haptic-feedback,immersive,tech",
            "oculus-vr-gloves-by-bighead",
            "oculus_vr_gloves.webp",
        ),
        (
            "E-Scooter",
            "Transport",
            "Fast, efficient, and eco-friendly. Great for city commuting! 🛴 It saves money, avoids traffic, and is just plain fun to ride. If you're looking for a cost-effective and sustainable way to travel, this is a fantastic option.",
            4,
            "electric-scooter,eco-friendly,commuting,tech,transport",
            "e-scooter-by-bighead",
            "e_scooter.jpg",
        ),
    ],
    "peter": [
        (
            "The Intelligent Investor",
            "Books",
            "A timeless classic in value investing. 📈 Benjamin Graham's principles on investing have stood the test of time, shaping the strategies of many successful investors, including Warren Buffett. The book emphasizes risk management, fundamental analysis, and long-term strategies. If you want to build wealth sustainably, this is the one book you need to read. The insights provided on market psychology and investment discipline make it invaluable for those who seek financial security rather than speculation.",
            4,
            "finance,investing,stocks,value-investing,long-term-strategy",
            "the-intelligent-investor-by-peter",
            "the_intelligent_investor.jpg",
        ),
        (
            "Soylent Meal Replacement",
            "Nutrition",
            "A complete meal in a bottle. 🚀 I have no time for inefficient activities like eating. Soylent provides all necessary nutrients in a convenient liquid form, reducing decision fatigue and optimizing productivity. It allows one to remain focused on important work while ensuring proper nutrition. The taste is neutral, but efficiency is what matters. Highly recommended for entrepreneurs, investors, and those who prioritize time efficiency over conventional habits.",
            4,
            "nutrition,productivity,health,meal-replacement,startup-culture",
            "soylent-meal-replacement-by-peter",
            "soyalent_meal_replacement.jpg",
        ),
        (
            "SpaceX Starlink",
            "Technology",
            "The future of global connectivity. 🌍 SpaceX's Starlink is solving one of the greatest technological limitations—providing high-speed internet anywhere on the planet. This project will not only democratize internet access but also unlock economic opportunities in remote regions. With continued advancements, the technology will be instrumental in future space missions and off-world colonies. I consider Starlink one of the most promising investments in global infrastructure.",
            4,
            "technology,space,internet,connectivity,innovation",
            "spacex-starlink-by-peter",
            "spacex_starlink.jpg",
        ),
        (
            "MacBook Pro M3 Max",
            "Laptops",
            "Efficiency, power, and longevity. 💻 The M3 Max is the most powerful MacBook yet, delivering unparalleled speed and battery life. Its ARM-based architecture optimizes power consumption while maintaining extreme performance, making it an essential tool for high-level computational tasks. Investors, entrepreneurs, and engineers alike can benefit from its capabilities. If you value productivity and reliability, this is the only laptop worth considering.",
            4,
            "apple,tech,productivity,laptops,hardware",
            "macbook-pro-m3-max-by-peter",
            "macbook_pro_m3_max.avif",
        ),
        # (
        #     "AI-Powered Investment Analytics",
        #     "Finance",
        #     "The inevitable future of investing. 🤖 AI is reshaping financial markets, enabling real-time predictive analysis and automated trading strategies. Machine learning models can now identify patterns in market fluctuations better than human analysts. Those who leverage AI-driven insights today will dominate the market in the next decade. Adapt now, or be left behind.",
        #     4,
        #     "ai,finance,investment,trading,technology",
        #     "ai-investment-analytics-by-peter",
        # ),
    ],
    "ron": [
        (
            "LegalZoom Business Services",
            "Legal",
            "The easiest way to handle legal paperwork without losing your mind. 📝 As a lawyer, I understand how overwhelming contracts and business formations can be. LegalZoom simplifies the entire process, making it accessible for startups, freelancers, and small business owners. Whether you're incorporating a company, filing trademarks, or drafting agreements, this platform is a great way to stay compliant without breaking the bank.",
            4,
            "legal,startup,law,business,contracts",
            "legalzoom-business-services-by-ron",
            "legal_zoom.jpg",
        ),
        (
            "Patagonia Duffel Bag",
            "Bags",
            "The perfect bag for a lawyer who surfs. 🌊 Whether I'm heading to a client meeting or escaping to the beach after, this bag is durable, stylish, and water-resistant. It fits everything I need, from legal briefs to board shorts. If you're a professional who appreciates function and adventure, this is the bag for you.",
            4,
            "travel,gear,lawyer-life,outdoors,patagonia",
            "patagonia-duffel-bag-by-ron",
            "patagonia_duffel_bag.jpg",
        ),
        (
            "Tesla Cybertruck",
            "Cars",
            "The ultimate lawyer-approved flex. 🚘 This futuristic tank on wheels is bulletproof, electric, and undeniably ridiculous—exactly what I need for high-stakes client meetings. It's powerful, sustainable, and makes me feel like a post-apocalyptic warlord pulling up to a deposition. 10/10 would recommend.",
            4,
            "cars,tech,tesla,sustainability,electric-vehicles",
            "tesla-cybertruck-by-ron",
            "tesla_cybertruck.jpg",
        ),
        (
            "Wolfram Alpha Legal Research Tool",
            "Software",
            "AI is making lawyers obsolete, and I'm here for it. 🤖 This tool automates legal research with unparalleled accuracy, saving me countless hours digging through case law. Instead of drowning in legal jargon, I can focus on what really matters—negotiating the best deals and hitting the beach by 3 PM. Every modern lawyer should be using AI-powered legal assistants. Adapt or get left behind.",
            4,
            "law,ai,legal-tech,productivity,research",
            "wolfram-alpha-legal-research-by-ron",
            "wolfam_alpha_legar_research_tool.png",
        ),
        (
            "CBD Gummies",
            "Wellness",
            "Law is stressful. Chill out. 🍃 These gummies help take the edge off after long days of intense negotiations and corporate drama. They help with focus, relaxation, and staying cool under pressure. Every lawyer should have a stash of these in their desk drawer. Just saying.",
            4,
            "wellness,relaxation,lawyer-life,stress-relief,cbd",
            "cbd-gummies-by-ron",
            "cbd_gummies.jpg",
        ),
    ],
    "carla": [
        (
            "Raspberry Pi 4",
            "Hardware",
            "This tiny computer is an absolute powerhouse for DIY projects. 🔧 As a hardware hacker, I love how versatile it is—you can build anything from a media center to a smart home hub with this. The improved processing power and connectivity options make it better than ever. Perfect for tinkerers and engineers who love getting their hands dirty with real tech.",
            4,
            "hardware,diy,tech,raspberry-pi,engineering",
            "raspberry-pi-4-by-carla",
            "raspberrypi5.webp",
        ),
        (
            "Flipper Zero",
            "Hacking Gadgets",
            "A must-have for hardware enthusiasts and ethical hackers. 🛠️ This pocket-sized multitool is perfect for experimenting with RFID, NFC, and signal analysis. I use it for security testing and debugging embedded systems. It's an absolute game-changer for anyone interested in cybersecurity and reverse engineering.",
            4,
            "hacking,cybersecurity,rfid,hardware,reverse-engineering",
            "flipper-zero-by-carla",
            "flipper_zero.jpg",
        ),
        (
            "Framework Laptop",
            "Laptops",
            "Finally, a laptop that respects repairability and modularity! 🔩 As someone who believes in fixing rather than replacing, I love that the Framework Laptop allows me to swap components and upgrade parts without throwing away the whole machine. This is how tech should be—customizable, sustainable, and free from corporate greed.",
            4,
            "laptops,repairability,modular,customization,sustainability",
            "framework-laptop-by-carla",
            "framework_laptop.jpg",
        ),
        (
            "Hak5 WiFi Pineapple",
            "Security",
            "If you're serious about WiFi security, you need this tool. 🖧 Whether you're testing for vulnerabilities or monitoring network security, the WiFi Pineapple is the gold standard for ethical hackers. It's scary how many networks are wide open—this device helps identify and patch those risks before real attackers exploit them. Essential for penetration testers.",
            4,
            "security,networking,hacking,ethical-hacking,penetration-testing",
            "hak5-wifi-pineapple-by-carla",
            "hak5_wifi_pineapple.jpg",
        ),
        (
            "Thermal Paste - Arctic MX-6",
            "PC Components",
            "If you're still using stock thermal paste, you're doing it wrong. ❄️ A proper cooling setup starts with high-quality thermal paste, and Arctic MX-6 delivers the best performance. Lower temps, better overclocking potential, and longer CPU lifespan. If you love custom PC builds, this is an absolute must-have.",
            4,
            "pc-builds,hardware,overclocking,thermal-management,cooling",
            "thermal-paste-arctic-mx6-by-carla",
            "thermal+paste+arctic_mx_6.webp",
        ),
    ],
}


class Command(BaseCommand):
    """Command class"""

    help = "Bulk create Silicon Valley inspired product reviews"

    def handle(self, *args, **kwargs):  # pylint: disable=unused-argument
        users = {
            user.username: user
            for user in User.objects.filter(username__in=USERS_REVIEWS.keys())
        }
        reviews_to_create = []

        for username, reviews in USERS_REVIEWS.items():
            user = users.get(username)
            if not user:
                continue

            for product_name, category, content, rating, tags, slug, image in reviews:
                local_image_path = os.path.join(LOCAL_IMAGE_FOLDER, image)
                new_image_path = os.path.join(MEDIA_FOLDER, image)

                if os.path.exists(local_image_path):
                    shutil.copy(local_image_path, new_image_path)
                    image_path = f"reviews/{image}"
                else:
                    image_path = None

                review = Review(
                    user=user,
                    product_name=product_name,
                    category=category,
                    content=content,
                    tags=tags,
                    rating=rating,
                    image=image_path,
                    slug=slug,
                )
                reviews_to_create.append(review)

        Review.objects.bulk_create(reviews_to_create)

        self.stdout.write(
            self.style.SUCCESS(  # pylint: disable=no-member
                f"✅ Successfully created {len(reviews_to_create)} product reviews!"
            )
        )
