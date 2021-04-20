autoscale: true
slidenumbers: true
footer: Thibault Vieux, Software Engineer @PayFit

# Sécurité réseau

![](https://user-images.githubusercontent.com/3305685/111139565-927ef000-8581-11eb-869f-514cce5c8714.png)

---

# Questions

[https://app.sli.do](https://app.sli.do/event/l2lknjii)

**Code:** #22671

---

# Qu'est ce que la sécurité réseau ?

Ensemble de pratique permettant de protéger

- **Les données**
  - Mauvais usage
  - Modification sans autorisation
  - Destruction
- **L'accès aux données**
  - Limité aux personnes ayant reçu l'accès

---

> Connais ton ennemi et connais-toi toi-même; eussiez-vous cent guerres à soutenir, cent fois vous serez victorieux.
> -- Sun Tzu, L’Art de la guerre

![](https://user-images.githubusercontent.com/3305685/111806468-4d84f180-88d2-11eb-9518-c00d4db1a38a.jpg)

---

Nous sommes en guerre contre:

- Hackers
- Scammers
- Script kiddies

Le champs de bataille sont les réseaux et le prix nos données.

^ Nous allons apprendre à connaître nos ennemis, leurs motivations, leurs méthodes et leurs attaques. Nous allons également étudier nos armes défensives et nos contre-attaques.

---

# Les règles de base de la sécurité informatique

Une sécurité efficace repose sur 3 éléments principaux:

- Confidentialité
- Intégrité
- Disponibilité

---

# La confidentialité

Seules les personnes autorisées peuvent avoir accès aux informations qui leur sont destinées. Tout accès indésirable doit être empêché.

- Chiffrement (ex: AES, RSA)
- Contrôle d'accès (ex: mot de passe, rbac)
- Authenticité (MFA)

---

# L'intégrité

Les données doivent être celles que l'on attend, et ne doivent pas être altérées de façon fortuite, illicite ou malveillante.

- Checksum (ex: SUM32, CRC, Hamming code)

^ Détection des erreurs dues à la corruption de la transmission des données.

- Hachage (ex: SHA, MD5)

^ Garantir l'intégrité du message, s'assurer que personnes n'a altéré le message en premier lieu.

---

# La disponibilité

L'accès aux ressources doit être permanent et sans faille durant les plages d'utilisation prévues.

- Redondance
- Scalabilité
- Firewall

---

D'autres aspects peuvent aussi être considérés comme des objectifs de la sécurité des SI, tels que :

- **La traçabilité**: Les accès et tentatives d'accès aux données sont tracés, ces traces sont conservées et exploitables.
  --> Datadog
- **La non-répudiation**: Aucun utilisateur ne doit pouvoir contester les opérations qu'il a réalisées dans le cadre de ses actions autorisées et aucun tiers ne doit pouvoir s'attribuer les actions d'un autre utilisateur.
  --> Certificat électronique (OpenPGP, X.509)

---

![](https://m4v4t9q2.rocketcdn.me/wp-content/themes/JointsWP/assets/videos/modele-osi-reseau.mp4)

^ https://www.napsis.fr/actualite/reseau-modele-osi/

---

# Le modèle OSI

![inline](https://user-images.githubusercontent.com/3305685/112309122-416aac80-8ca3-11eb-8226-63fefad1948f.png)

---

# Les modèles OSI et TCP/IP

![inline](https://user-images.githubusercontent.com/3305685/112558925-25b0f480-8dd0-11eb-841e-e64897c6e60f.png)

---

![](https://user-images.githubusercontent.com/3305685/111807567-5924e800-88d3-11eb-95b2-4205987a40a0.jpeg)

^ Attaque par déni de service

^ Le but est de rendre indisponible un service, d'empêcher les utilisateurs légitimes d'un service de l'utiliser.

---

# [DOS Taxonomie](http://www.cs.cornell.edu/courses/cs619/2004fa/documents/taxonomy-ccr.pdf): Quiz n°1

[.column]

# Attaques:

- Random Scanning
- Permutation Scanning
- Signpost Scanning
- Hitlist Scanning

[.column]

# Descriptions:

1. Une partie de la liste des cibles est fournie à un ordinateur compromis.
2. Tous les ordinateurs compromis partagent une permutation pseudo-aléatoire commune de l'espace d'adressage IP.
3. Utilise les modèles de communication de l'ordinateur compromis pour trouver une nouvelle cible.
4. Chaque ordinateur compromis sonde des adresses aléatoires.

^ 4, 2, 3, 1

^ Scanner un réseau afin de recruter des machines vulnérables sans se faire détecter

^ Classification par stratégie de scan

---

# [DOS Taxonomie](http://www.cs.cornell.edu/courses/cs619/2004fa/documents/taxonomy-ccr.pdf): Quiz n°2

[.column]

# Attaques:

- Subnet Spoofing
- Random Spoofing
- Fixed Spoofing

[.column]

# Descriptions:

1. Génére des nombres de 32 bits et tamponne les paquets avec
2. Génére des adresses aléatoires dans un espace d'adressage donné
3. L'adresse usurpée est l'adresse de la cible.

^ 2, 1, 3

^ Spoofing: Usurpation d'identité, changer l'IP source

^ Classification par validité de l'IP source

---

# [DOS Taxonomie](http://www.cs.cornell.edu/courses/cs619/2004fa/documents/taxonomy-ccr.pdf): Quiz n°3

[.column]

# Attaques:

- Server Application
- Network Access
- Infrastructure

[.column]

# Descriptions:

1. La motivation de cette attaque est un service crucial d'Internet, par exemple, un routeur central.
2. L'attaque vise une application spécifique sur un serveur.
3. L'attaque est utilisée pour surcharger ou faire tomber le mécanisme de communication d'un réseau.

^ 2, 3, 1

^ Classification par type de victime

---

![inline](https://user-images.githubusercontent.com/3305685/112140746-b3c08b80-8bd4-11eb-9831-f8a020800267.png)

---

# Network DoS

[.column]

## **Objectif:** Rendre inaccessible un service avec peu de ressources

**Comment ?**

Via une attaque par amplification!

- Un petit nombre de paquets
- Gros impact sur les ressources

[.column]

![inline](https://digistatement.com/wp-content/uploads/2020/04/IMG_20200423_191314.jpg)

---

# Network DoS

Deux types d'attaques par amplification:

[.column]

**DoS bug:**

- Défaut de conception permettant à une machine de perturber un service

[.column]

**DoS flood:**

- Commandez un réseau de robots pour générer un grand volume de requêtes

^ DoS bug: Une requête serveur qui demande beaucoup de ressource à la base de données car les données ne sont pas mise en cache. Une gestion de la pagination trop permissive. Une requête non conforme qui fait planter le serveur à cause d'une mauvaise gestion des erreurs.

---

![](https://user-images.githubusercontent.com/3305685/112163005-e1b1ca00-8bec-11eb-8663-5e3acc2180f5.png)

^ Couche liaison: Un gros traffic de données pour saturer les routeurs.

^ Couche transport TCP/UDP: Par exemple le serveur a besoin d'utiliser des ressources mémoires afin de garder un état des connections TCP. Ainsi l'attaquant peut envoyer plein de paquets TCP pour épuiser la mémoire du serveur.

^ Couche application: Par exemple l'attaquant peut demander au serveur de récupérer un gros volume de données, si ces demandes sont nombreuses, les ressources du serveur seront épuisées.

---

# Attaque par amplification

[.column]

![inline](https://user-images.githubusercontent.com/3305685/112155955-1a01da00-8be6-11eb-8af2-4b4baaf4da18.png)

[.column]

# NTP - Network Time Protocol

Permet de synchroniser, via un réseau informatique, l'horloge locale d'ordinateurs sur une référence d'heure.

^ Lorsqu'un ordinateur demande l'heure au serveur NTP, le volume de données envoyé par une machine au serveur est beaucoup plus faible que la réponse du serveur.

^ https://www.cloudflare.com/fr-fr/learning/ddos/ntp-amplification-ddos-attack/

---

# Amplification Quiz

Lesquelles de ces raisons expliquent pourquoi le protocole NTP basé sur le protocole UDP est particulièrement vulnérable aux attaques par amplification ?

- [ ] Une petite commande peut générer une réponse importante.
- [ ] Vulnérable à l'usurpation de l'IP source.
- [ ] Il est difficile de s'assurer que les ordinateurs ne communiquent qu'avec des serveurs NTP légitimes.

^ Vrai: Le volume de la requête provenant de notre ordinateur est plus faible que le volume de données provenant de la réponse du serveur.

^ Vrai: L'attaque fonctionne car il est possible d'usurper l'identité de la source IP afin que la réponse soit redirigé vers la machine que l'on souhaite attaquer.

^ Vrai: Il est difficile de filtrer les réponses des serveurs NTP.

---

![](https://user-images.githubusercontent.com/3305685/112167158-87b30380-8bf0-11eb-879c-0aa50dba0db5.png)

---

# Example d'amplification

![inline](https://user-images.githubusercontent.com/3305685/112171502-2ab94c80-8bf4-11eb-8e03-ad8dfa8f88b0.jpg)

2006: 0.58M open resolvers on Internet (Kaminsky-Shiffman)
2014: 28M open resolvers (openresolverproject.org)

^ https://www.cloudflare.com/fr-fr/learning/ddos/dns-amplification-ddos-attack/

---

![](https://user-images.githubusercontent.com/3305685/112174561-cd72ca80-8bf6-11eb-93b6-790c917a52bc.png)

---

![Course+Notes-Denial+of+Service+Attacks_page-0012](https://user-images.githubusercontent.com/3305685/112178240-e761dc80-8bf9-11eb-95ee-1a7db2de0edc.jpg)

---

![Course+Notes-Denial+of+Service+Attacks_page-0013](https://user-images.githubusercontent.com/3305685/112178242-e761dc80-8bf9-11eb-8444-e7b95253202f.jpg)

---

![Course+Notes-Denial+of+Service+Attacks_page-0014](https://user-images.githubusercontent.com/3305685/112178243-e7fa7300-8bf9-11eb-8e7e-1f249294aa7d.jpg)

---

![Course+Notes-Denial+of+Service+Attacks_page-0015](https://user-images.githubusercontent.com/3305685/112178245-e8930980-8bf9-11eb-8965-875d1d3a8379.jpg)

^ Blaster a exploité une vulnérabilité de type dépassement de tampon qui était présente dans le service DCOM RPC de Windows XP/2000. Il se propageait rapidement vers des adresses IP générées aléatoirement. Une fois infecté, l’ordinateur s’éteignait après 60 secondes. Le ver était programmé pour commencer une attaque (quatre jours après son apparition) de type SYN flood sur le site des mises à jour Windows (windowsupdate.com), ce qui a forcé Microsoft à rediriger le site vers un autre nom de domaine.

---

![Course+Notes-Denial+of+Service+Attacks_page-0016](https://user-images.githubusercontent.com/3305685/112178248-e8930980-8bf9-11eb-9b03-06fd69763577.jpg)

---

![Course+Notes-Denial+of+Service+Attacks_page-0017](https://user-images.githubusercontent.com/3305685/112178252-e92ba000-8bf9-11eb-8eef-fa44293a308f.jpg)

^ https://www.cert-ist.com/public/fr/SO_detail?code=Syn_Cookies

---

# Cookies SYN Quiz

- [ ] Les cookies SYN nécessite une version modifié de TCP.
- [ ] Les cookies SYN entraînent un ralentissement général des performances.
- [ ] Le serveur rejete les options TCP car la file d'entrée n'est plus accessible lors du SYN.

^ Faux, un SYN Cookie est un choix particulier de numéro de séquence Initial (ISN) effectué par un serveur lors d'une demande de connexion TCP.

^ Faux, ils ne sont appliqués que lors d'une attaque SYN Flood.

^ Vrai, l'état de la connection n'est pas conservé en mémoire sur le serveur.

---

![Course+Notes-Denial+of+Service+Attacks_page-0019](https://user-images.githubusercontent.com/3305685/112178259-e9c43680-8bf9-11eb-966e-d9afa1f494fe.jpg)

---

![Course+Notes-Denial+of+Service+Attacks_page-0020](https://user-images.githubusercontent.com/3305685/112178263-ea5ccd00-8bf9-11eb-8bce-01cf429e4e47.jpg)

---

![Course+Notes-Denial+of+Service+Attacks_page-0021](https://user-images.githubusercontent.com/3305685/112178265-eaf56380-8bf9-11eb-9c00-23eefb3db278.jpg)

---

![Course+Notes-Denial+of+Service+Attacks_page-0022](https://user-images.githubusercontent.com/3305685/112178267-eaf56380-8bf9-11eb-8dec-0e36ef96d8cf.jpg)

^ L'idée est de prendre un serveur populaire utilisé par de nombreux utilisateur (ex: Baidu) et d'y injecter un script malveillant qui va s'exécuter côté client.

---

# A real-work example: GitHub (3/2015)

Le script ci-dessous crée une balise image sur la page que vous visitez 100x/seconde. Chaque visiteur du site infecté devient un participant involontaire à une attaque DDoS contre Github.

```javascript
function imgFlood() {
  let pic = new Image();
  let TARGET = "user-images.githubusercontent.com";
  let rand = Math.floor(Math.random() * 1000);
  pic.src = "https://" + TARGET + "/" rand + ".jpg";
}
setInterval(imgFlood, 10);
```

<sub>Source: [Cloudflare - An introduction to JS based DDoS](https://blog.cloudflare.com/an-introduction-to-javascript-based-ddos/)</sub>

^ Les messages envoyés par le navigateur sont des requêtes HTTP valides, ce qui en fait une attaque de niveau 7.

---

# Attaque par inondation UDP Quiz

- [ ] Les attaquants peuvent usurper l'adresse IP de leurs paquets UDP.
- [ ] L'attaque peut être atténuée avec un pare-feu.
- [ ] Les pare-feu ne peuvent pas arrêter une inondation car ils y sont vulnérables.

^ Vrai: Les attaquants peuvent usuper l'adresse IP.

^ Faux: Les pare-feu ne peuvent pas atténuée l'attaque car ils semblent tous légitimes.

^ Vrai: Même si le firewall tente de filtrer le traffic, il est lui-même sensible à l'attaque car il doit examiner un grand nombre de paquets.

---

![Course+Notes-Denial+of+Service+Attacks_page-0025](https://user-images.githubusercontent.com/3305685/112178273-ec269080-8bf9-11eb-81fa-79f692961133.jpg)

^ Détournement du routage d'adresse IP

^ En février 2008, Pakistan Telecom a fait tomber par inadvertance l'ensemble du site YouTube dans le monde entier pendant deux heures alors qu'il tentait de restreindre l'accès local au site. Lorsque Pakistan Telecom a essayé de filtrer l'accès à YouTube, il a envoyé de nouvelles informations de routage via BGP à PCCW, un ISP de Hong Kong qui a propagé les fausses informations de routage sur Internet.

---

![Course+Notes-Denial+of+Service+Attacks_page-0026](https://user-images.githubusercontent.com/3305685/112178275-ec269080-8bf9-11eb-89c8-8195d6ddab78.jpg)

^ Le service Youtube a été inaccessible pendant 2 heures. Contactant dans un premier temps Pakistan Telecom, puis en définissant un masque de sous-réseau plus petit en attendant que la situation soit corrigé.

---

![Course+Notes-Denial+of+Service+Attacks_page-0028](https://user-images.githubusercontent.com/3305685/112178278-ecbf2700-8bf9-11eb-8cd2-efcaeacaff5f.jpg)

^ Le client peut générer une clé secrète partagée entre le client et le serveur et la chiffrer à l'aide de la clé publique du serveur. Lorsque le serveur reçoit la clé chiffrée, il utilise sa clé privée pour la déchiffrer et extraire la clé secrète.

^ Le déchiffrage RSA est 10x plus coûteux que le chiffrage

^ De manière similaire le client peut demander via une requête HTTP de nombreux fichiers PDF volumineux.

---

![Course+Notes-Denial+of+Service+Attacks_page-0029](https://user-images.githubusercontent.com/3305685/112178280-ed57bd80-8bf9-11eb-94b6-60762d4ad5c4.jpg)

^ Pour ralentir l'attaquant on peut demander au client de résoudre un challenge.

---

![Course+Notes-Denial+of+Service+Attacks_page-0030](https://user-images.githubusercontent.com/3305685/112178286-edf05400-8bf9-11eb-9fdb-4228dd475ad2.jpg)

---

![Course+Notes-Denial+of+Service+Attacks_page-0031](https://user-images.githubusercontent.com/3305685/112178287-edf05400-8bf9-11eb-96d9-b7ad2242de80.jpg)

---

![Course+Notes-Denial+of+Service+Attacks_page-0032](https://user-images.githubusercontent.com/3305685/112178292-ee88ea80-8bf9-11eb-9e65-764fff5176af.jpg)

---

![Course+Notes-Denial+of+Service+Attacks_page-0033](https://user-images.githubusercontent.com/3305685/112178298-ee88ea80-8bf9-11eb-9406-a09f7bc929cf.jpg)

^ La difficulté du puzzle peut-être ajusté en fonction de l'intensité de l'attaque que subis le serveur.

---

![Course+Notes-Denial+of+Service+Attacks_page-0034](https://user-images.githubusercontent.com/3305685/112178301-ef218100-8bf9-11eb-905c-81614dc578d4.jpg)

^ Une autre variante de ces puzzles consiste à utiliser des fonctions liées à la mémoire car ceux-ci s'adapte mieux aux machines bas de gamme.

---

![Course+Notes-Denial+of+Service+Attacks_page-0035](https://user-images.githubusercontent.com/3305685/112178303-ef218100-8bf9-11eb-989a-a33ad358834b.jpg)

---

# Puzzle Quiz

Lesquelles de ces hypothèses sont vraies ?

- [ ] Les énigmes des clients doivent être difficiles à construire. C'est une indication du niveau de difficulté pour les résoudre.
- [ ] Les énigmes des clients doivent être "stateless".
- [ ] La complexité des énigmes doit augmenter avec la puissance de l'attaque.

^ Faux: Les énigmes ne doivent pas être difficile a construire par le serveur.

^ Vrai: Cela permet d'éviter que le client puisse deviner le puzzle en amont.

^ Vrai

---

![Course+Notes-Denial+of+Service+Attacks_page-0037](https://user-images.githubusercontent.com/3305685/112178306-efba1780-8bf9-11eb-923c-2a68b0223657.jpg)

^ Le serveur vérifie que la connection provient d'un être humain au lieu d'un bot ou un malware.

---

![Course+Notes-Denial+of+Service+Attacks_page-0038](https://user-images.githubusercontent.com/3305685/112178310-f052ae00-8bf9-11eb-89d7-eb90b8e72c5b.jpg)

^ Cette protection se situe au niveau de la couche application

^ Présente un CAPTCHA par addresse IP source

---

# DoS Mitigation: Source Identification

**Objectif:** Identifier la source du packet

**Objectif ultime:** Bloquer l'attaque à la source

---

![Course+Notes-Denial+of+Service+Attacks_page-0040](https://user-images.githubusercontent.com/3305685/112178316-f052ae00-8bf9-11eb-905b-c26167c29de8.jpg)

^ Ce problème peut paraître simple à résoudre.

^ La plupart des paquets impliqués dans une attaque DoS ont une adresse IP source usurpée ou aléatoire.

^ Pourquoi ne pas demander aux FAI de filtrer les adresses sources qui ne sont pas légitimes ?

---

![Course+Notes-Denial+of+Service+Attacks_page-0041](https://user-images.githubusercontent.com/3305685/112178319-f0eb4480-8bf9-11eb-81f0-c32d5f6f323a.jpg)

^ Si le routeur s'attend à ce que tout le trafic provienne d'un préfixe particulier, il peut supprimer tous les paquets dont l'adresse source est différente de ce préfixe.

---

![Course+Notes-Denial+of+Service+Attacks_page-0042](https://user-images.githubusercontent.com/3305685/112178323-f0eb4480-8bf9-11eb-9ae1-02cf6f25474d.jpg)

^ Filtrage à l'entrée - Problèmes de mise en œuvre

^ Nécessite une confiance globale car tous les FAI doivent le faire.

^ Inutile si seulement 10% des FAI ne le font pas.

^ Aucune incitation au déploiement

---

![Course+Notes-Denial+of+Service+Attacks_page-0043](https://user-images.githubusercontent.com/3305685/112178326-f183db00-8bf9-11eb-8ee8-4234a08ae925.jpg)

---

![Course+Notes-Denial+of+Service+Attacks_page-0044](https://user-images.githubusercontent.com/3305685/112178327-f183db00-8bf9-11eb-89e0-5194bd678845.jpg)

---

![Course+Notes-Denial+of+Service+Attacks_page-0045](https://user-images.githubusercontent.com/3305685/112178330-f21c7180-8bf9-11eb-8ae7-ee0dfd15cf06.jpg)

---

# DoS Mitigation: Edge Sampling

- **Edge:** Adresse IP de **début** et de **fin**
- **Distance:** Nombre de sauts depuis la dernière arête enregistré

---

# DoS Mitigation: Edge Sampling

L'algo suivant permet au routeur de décider comment enregistrer l'information pour chaque arête. Lorsqu'un paquet arrive, il tire à pile ou face 🪙

[.column]

Si c'est **pile**

- Il inscrit son adresse dans l'**adresse de départ**
- Il écrit 0 dans le champ **distance**

[.column]

Si c'est **face**

- Si la distance est de 0, il écrit son adresse IP dans le champ de l'**adresse de fin**
- Il incrémente le champ **distance**.

---

![Course+Notes-Denial+of+Service+Attacks_page-0049](https://user-images.githubusercontent.com/3305685/112178339-f34d9e80-8bf9-11eb-8f9c-66f8edd1d20f.jpg)

^ R1 reçoit un paquet depuis la source ou un autre routeur.

^ Le paquet contient un espace pour écrire le début, la fin et la distance.

---

![Course+Notes-Denial+of+Service+Attacks_page-0050](https://user-images.githubusercontent.com/3305685/112178343-f3e63500-8bf9-11eb-9a94-21764beb117b.jpg)

^ Pile: Le routeur R1 inscrit son adresse dans l'adresse de départ et défini la distance à 0.

---

![Course+Notes-Denial+of+Service+Attacks_page-0051](https://user-images.githubusercontent.com/3305685/112178344-f47ecb80-8bf9-11eb-98bb-8e3bf3c7a717.jpg)

^ Face: Le routeur R2 inscrit son adresse dans l'adresse de fin car la distance est de 0, puis il incrémente le champ distance.

---

![Course+Notes-Denial+of+Service+Attacks_page-0052](https://user-images.githubusercontent.com/3305685/112178345-f47ecb80-8bf9-11eb-935b-3d7c73ab9700.jpg)

^ Face: Le routeur R3 incrémente le champ distance et ne touche pas à l'adresse de fin car la distance est supérieure à 0.

^ Pour le routeur R3, la distance pour aller a R1 est de 2.

---

# DoS Mitigation: Edge Sampling

Reconstruction du chemin:

- Extraire l'information des paquets de l'attaquant
- Construire un graphe orienté
  - Chaque tuple (début, fin, distance) fourni une arête du graphe
- Une formule mathématique permet ensuite de déterminer le **nombre de paquets nécessaire** pour reconstruire le graphe en fonction de la **distance de l'attaquant**

---

# Edge Sampling Quiz

Lesquelles de ces hypothèses concernant le Edge Sampling sont vraies ?

- [ ] Il permet d'identifier plusieurs attaquants
- [ ] Il est difficile pour les victimes de reconstruire un chemin vers l'attaquant
- [ ] Nécessite de l'espace dans l'en-tête du paquet IP.

^ Vrai: En reconstruisant le graphe on peux récupérer plusieurs sources et donc plusieurs attaquants.

^ Faux

^ Vrai

---

![Course+Notes-Denial+of+Service+Attacks_page-0055](https://user-images.githubusercontent.com/3305685/112178353-f5aff880-8bf9-11eb-8277-883442bd74cf.jpg)

^ L'attaquant usurpe l'adresse IP de la victime et envoie des requêtes DNS à de nombreux serveurs DNS. Les réponses sont ensuite envoyées à l'adresse IP de la victime.

---

![Course+Notes-Denial+of+Service+Attacks_page-0056](https://user-images.githubusercontent.com/3305685/112178356-f5aff880-8bf9-11eb-9665-ee974b4a8f44.jpg)

^ Il existe d'autres attaques par réflexion qui utilise des serveurs web et des serveurs P2P tel que Gnutella.

---

![Course+Notes-Denial+of+Service+Attacks_page-0057](https://user-images.githubusercontent.com/3305685/112178358-f6488f00-8bf9-11eb-9fb1-fa4d25a60f72.jpg)

^ Une attaque par réflecteur est généralement contrôlé par une personne contrôlant de nombreux robots qui vont envoyer des requêtes sur de nombreux serveurs. Cela aura pour résultat d'inonder la victime sous un gros volume de données.

^ Un système de traçage permettra de remonter les paquets d'attaque jusqu'aux réflecteurs, mais comme ces derniers n'effectuent aucun marquage et ne conservent aucun état, il n'y a aucune possibilité de remonter jusqu'aux bots.

---

# Reflector Attack Quiz

L'autodéfense contre les attaques par réflecteur doit incorporer :

- [ ] Filtrage - filtrer le trafic DNS aussi près que possible de la victime.
- [ ] Redondance des serveurs - les serveurs doivent être situés dans plusieurs réseaux et pays.
- [ ] Limitation du trafic - le trafic provenant d'un serveur DNS doit être limité à des seuils raisonnables.

^ Faux: Le filtrage doit se faire au plus proche de l'attaquant, càd le plus loin possible de la victime.

^ Vrai: Cela permet de répartir la charge de l'attaque sur plusieurs serveurs.

^ Vrai: Dans l'idéal, les résolveurs DNS ne devraient fournir leurs services qu'à des appareils qui proviennent d'un domaine de confiance.

---

![Course+Notes-Denial+of+Service+Attacks_page-0059](https://user-images.githubusercontent.com/3305685/112178362-f6e12580-8bf9-11eb-8c4f-678697630c8c.jpg)

^ Quelques idées novatrices pour se défendre contre les DoS.

^ Il y a plusieurs exemple qui se basent sur un système de capabilités.

---

![Course+Notes-Denial+of+Service+Attacks_page-0060](https://user-images.githubusercontent.com/3305685/112178363-f6e12580-8bf9-11eb-8e55-ff18489fec7d.jpg)

^ Au lieu de pouvoir envoyer n'importe quoi à n'importe qui et n'importe quand, les clients doivent d'abord obtenir la "permission" d'envoyer des données au serveur; le serveur fournit en retour des jetons (capabilités) aux clients dont il accepte le trafic. Les clients incluent ensuite ces jetons dans leurs paquets.

^ Similaire au standard JSON Web Token qui permet l'échange sécurisé de jetons entre plusieurs parties. Cette sécurité de l’échange se traduit par la vérification de l’intégrité des données à l’aide d’une signature numérique (HMAC/RSA).

---

![Course+Notes-Denial+of+Service+Attacks_page-0061](https://user-images.githubusercontent.com/3305685/112178365-f779bc00-8bf9-11eb-9337-e2c0710b948c.jpg)

^ Cela permet d'avoir des points de vérification répartis sur le réseau afin de vérifier que le trafic est légitime. Les capacités peuvent être révoquées si la source est malveillante aux niveaux des routeurs de façon à être au plus proche de l'attaquant.

---

![Course+Notes-Denial+of+Service+Attacks_page-0062](https://user-images.githubusercontent.com/3305685/112178367-f779bc00-8bf9-11eb-8606-fa4cad25da8e.jpg)

---

![](https://i1.wp.com/lifars.com/wp-content/uploads/2020/04/Do-you-know-why-Cyber-Crime-Happens-scaled.jpg?fit=2560%2C1440&ssl=1)

^ Dans cette leçon, nous allons examiner la cybercriminalité, son économie et certaines des motivations des acteurs. À la fin de cette leçon, vous devriez avoir une bien meilleure compréhension de la frontière entre un commerce légitime et la cybercriminalité sur Internet.

---

![Course Notes Cybercrime_page-0001](https://user-images.githubusercontent.com/3305685/112466500-40e71a00-8d66-11eb-95b4-c9b0b3d45472.jpg)

^ Les développeurs découvrent des bugs pouvant être exploités afin de compromettre la sécurité de machines, ils les vendent pour faire du profit. Black Hat Hacker.

---

![Course Notes Cybercrime_page-0002](https://user-images.githubusercontent.com/3305685/112466514-43497400-8d66-11eb-9f8d-234ce6a89f94.jpg)

^ Il y a ensuite les bot masters qui vont créer et exploiter un réseau composé d'ordinateurs compromis.

^ Ils achètent des exploits, les transforment en malware (logiciels malveillants) qui vont permettre d'injecter une charge (payload) sur les machines vulnérables afin de les contrôler à distance.

^ Ils peuvent gagner de l'argent en louant le réseau de robots à d'autres acteurs malveillants (DDoS).

---

![Course Notes Cybercrime_page-0003](https://user-images.githubusercontent.com/3305685/112466521-447aa100-8d66-11eb-8746-3af9310c6535.jpg)

^ L'une des utilités d'un botnet est d'envoyer du spam.

^ Le bot master peut louer son réseau botnet à un spammeur, qui enverra à son tour du spam vers d'autres acteurs malveillants.

---

![Course Notes Cybercrime_page-0004](https://user-images.githubusercontent.com/3305685/112466528-45133780-8d66-11eb-874b-e6796ba8b8aa.jpg)

^ Les phishers sont un type de mauvais acteurs qui peuvent utiliser l'aide des spammeurs. Ils créent de faux sites afin de voler des informations telles que des comptes bancaires, des numéros de cartes de crédit, etc...

^ Ils peuvent demander aux spammeurs de rediriger du trafic vers le site malveillant en incluant l'URL dans l'email avec un message qui donne envie de cliquer dessus.

---

![Course Notes Cybercrime_page-0005](https://user-images.githubusercontent.com/3305685/112466530-46446480-8d66-11eb-96ec-218e80ccce76.jpg)

^ De même, les contrefacteurs utilisent des spams pour vendre leurs produits contrefaits.

---

![Course Notes Cybercrime_page-0006](https://user-images.githubusercontent.com/3305685/112466533-46dcfb00-8d66-11eb-999a-d919eb71c469.jpg)

^ Un mauvais acteur dans le cyberespace doit envisager la possibilité que ses activités, en particulier ses sites web, soient détectées et fermées par les forces de l'ordre.

^ Il doit donc trouver des fournisseurs de serveurs "bulletproof". Ces fournisseurs opèrent généralement dans des zones de non-droit et ils côutent chers.

---

![Course Notes Cybercrime_page-0007](https://user-images.githubusercontent.com/3305685/112466539-480e2800-8d66-11eb-927f-07769f48a7b3.jpg)

^ La majorité des mauvais acteurs sont là pour l'argent.

^ Ils volent vos comptes bancaires et vos cartes de crédit pour ensuite vider votre compte en passant par des services de blanchiment d'argent.

---

![Course Notes Cybercrime_page-0008](https://user-images.githubusercontent.com/3305685/112466541-48a6be80-8d66-11eb-96c2-6a87d0b71c24.jpg)

^ Le crowdturfing tire son nom d'une combinaison de crowdsourcing et d'astroturfing.

^ Consiste à amener un grand nombre de personnes à faire un petit geste pour atteindre un objectif, tandis que l’astroturf désigne des techniques de propagande manuelles utilisées à des fins publicitaires ou politique. Par exemple, le fait d'acheter des avis positif pour vendre un article bidon.

---

![Course Notes Cybercrime_page-0009](https://user-images.githubusercontent.com/3305685/112466544-493f5500-8d66-11eb-9df2-58dfbf5c07f8.jpg)

^ L'idée est que les acteurs malveillants forment un écosystème interconnecté parce que leurs activités se soutiennent mutuellement.

---

![Course Notes Cybercrime_page-0010](https://user-images.githubusercontent.com/3305685/112466553-4a708200-8d66-11eb-8d28-6b4a90cff8e3.jpg)

^ Les points d'entrée pour les acteurs malveillants sont les forums et les messageries chiffrés tel que Telegram. Ils s'en servent essentiellement pour se faire de la publicité.

---

![Course Notes Cybercrime_page-0011](https://user-images.githubusercontent.com/3305685/112466556-4b091880-8d66-11eb-98aa-71937e12f8a6.jpg)

^ Il est évident que les forces de l'ordre surveillent et peuvent fermer ces sites. Cependant, de nouveaux forums peuvent toujours apparaître et combler le vide.

---

![Course Notes Cybercrime_page-0012](https://user-images.githubusercontent.com/3305685/112466558-4ba1af00-8d66-11eb-9b68-dc48015ebaaa.jpg)

^ Ces forums constituent également des sources de données précieuses pour les chercheurs.

^ Par exemple, les chercheurs peuvent étudier les données pour connaître les nouvelles tendances et détecter les attaques en cours.

---

![Course Notes Cybercrime_page-0013](https://user-images.githubusercontent.com/3305685/112466563-4c3a4580-8d66-11eb-8b89-85ae3550a5e4.jpg)

^ Les forums sont remplis d'acheteurs, de vendeurs et d'escrocs.

^ Il y a des transactions honnêtes mais aussi des arnaques des acheteurs.

^ Ces forums sont réglementés par des administrateurs dans la limite de ce qu'ils peuvent gérer.

^ La plupart des messages sur les forums ne sont que des publicités.

---

![Course Notes Cybercrime_page-0014](https://user-images.githubusercontent.com/3305685/112466567-4cd2dc00-8d66-11eb-9cb5-be1953072243.jpg)

^ Par exemple, on peut annoncer qu'on a volé des comptes bancaires ou une liste d'adresses électroniques.

^ On peut proposer d'échanger un numéros de carte de crédit volés contre l'accès à une machine Linux piratée.

---

![Course Notes Cybercrime_page-0015](https://user-images.githubusercontent.com/3305685/112466570-4e040900-8d66-11eb-8a9e-1c6161448883.jpg)

^ Nombre de ces annonces contiennent des preuves, par exemple, en fournissant un échantillon des informations volées.

^ Le forum n'est généralement utile que pour faire de la publicité. La prise de décision réelle se fait généralement par le biais d'une messagerie privée.

---

![Course Notes Cybercrime_page-0017](https://user-images.githubusercontent.com/3305685/112466578-4fcdcc80-8d66-11eb-97c3-d802fe0515b1.jpg)

^ Par le passé, le fait de comprommetre des systèmes informatiques et en tirer profits étaient généralement le fait d'une même bande criminelle.

---

![Course Notes Cybercrime_page-0018](https://user-images.githubusercontent.com/3305685/112466579-50666300-8d66-11eb-9a34-d4b2405b92fe.jpg)

^ Aujourd'hui, les malfaiteurs sont spécialisés et remplissent différentes fonctions.

^ Par exemple, il existe des développeurs qui mettent au point des kits d'exploitation et les vendent à d'autres malfaiteurs.

^ Ces derniers sont chargés d'utiliser ces kits d'exploitation pour compromettre des ordinateurs. Par exemple, ils peuvent envoyer du spam avec un malware en pièce jointe. Une fois que l'utilisateur ouvre la pièce jointe, son ordinateur est compromis.

^ Ces ordinateurs compromis sont ensuite vendus sur le marché noir afin que d'autres malfaiteurs puissent les utiliser pour lancer des activités malveillantes et frauduleuses.

^ Et les mauvais acteurs sont ici payés selon le modèle du paiement à l'installation.

---

![Course Notes Cybercrime_page-0019](https://user-images.githubusercontent.com/3305685/112466584-51979000-8d66-11eb-9f68-99259caa3f26.jpg)

^ Discutons plus en détail des exploits-as-a-service, et en particulier du modèle de paiement par installation.

^ L'un des moyens de distribuer des logiciels malveillants, est ce que l'on appelle le "drive-by-download". En gros, un site web est compromis de manière à ce qu'un malware soit intégré dans ses scripts.

^ Ensuite lorsqu'un ordinateur client visite le site, le malware est installé son ordinateur.

---

![Course Notes Cybercrime_page-0020](https://user-images.githubusercontent.com/3305685/112466588-52302680-8d66-11eb-8b18-689425e16d8f.jpg)

^ Ce modèle de distribution des logiciels malveillants comporte deux éléments.

^ Le premier élément est que le malfaiteur a besoin du kit d'exploitation, car il permettra d'installer le logiciel malveillant sur les ordinateurs des victimes.

^ Le malfaiteur peut soit le déployer le kit lui-même sur un serveur, soit louer l'accès à un serveur qui héberge déjà le kit.

---

![Course Notes Cybercrime_page-0021](https://user-images.githubusercontent.com/3305685/112466591-53615380-8d66-11eb-8ba4-64c2ca95ae77.jpg)

^ Le deuxième élément de ce modèle de distribution de logiciels malveillants est que le malfaiteur doit faire en sorte que les ordinateurs concernés visitent le serveur d'exploitation afin que le logiciel malveillant s'intalle sur ces ordinateurs.

^ Le moyen le plus courant d'y parvenir est d'utiliser le spam ou le phishing pour attirer le trafic vers le serveur d'exploitation.

---

![Course Notes Cybercrime_page-0022](https://user-images.githubusercontent.com/3305685/112466592-53f9ea00-8d66-11eb-97a0-2329417c07b7.jpg)

^ Le Traffic-PPI simplifie ce processus de diffusion des logiciels malveillants.

^ Il combine essentiellement les deux éléments en un seul service.

^ Aujourd'hui le paiement par installation est le moyen le plus populaire qui est utilisé pour diffuser les logiciels malveillants.

---

# Dark Web Quiz

Associez chaque terme à une description :

[.column]

- [ ] Deep web
- [ ] Dark web
- [ ] Surface web

[.column]

1. Il est facilement accessible et consultable à l'aide de moteurs de recherche standard.

2. Il n'est pas indexé par les moteurs de recherche standard.

3. Il est la partie "cachée" d'internet et nécessite un logiciel spécifique tel que TOR.

^ 2, 3, 1

---

![Course Notes Cybercrime_page-0024](https://user-images.githubusercontent.com/3305685/112466596-552b1700-8d66-11eb-876f-c53936a7b9d1.jpg)

^ Lorsque nous pensons à internet, nous faisons généralement référence au web de surface. Le web de surface est en fait une toute petite partie de l'Internet.

---

![Course Notes Cybercrime_page-0025](https://user-images.githubusercontent.com/3305685/112466599-55c3ad80-8d66-11eb-920a-ec85518dd016.jpg)

^ Prenons un exemple de traffic pay per install.

^ Il y a 3 acteurs: les victimes, les développeurs d'exploits, et les clients (ou attaquants) qui utilisent les exploits pour distribuer les logiciels malveillants.

^ Si on regarde le flux de trafic, on remarque que le paiement provient les clients qui achètent ou louent les exploits aux développeurs d'exploits.

^ Le logiciel malveillant circule des attaquants vers la victime.

^ Le montant du paiement dépend du volume d'installation du malware.

---

# PPI Quiz

Accordez chaque terme à sa définition :

[.column]

- [ ] Doorway pages (pages satellite)
- [ ] Crypters
- [ ] Blackhat Search Engine Optimizer
- [ ] Trojan Download Manager

[.column]

1. Un programme qui cache les codes malveillants aux logiciels anti-virus.
2. Un logiciel qui permet à un attaquant de mettre à jour ou d'installer des logiciels malveillants sur l'ordinateur d'une victime.
3. Il augmente le trafic vers le site de l'attaquant en manipulant les moteurs de recherche.
4. Une page Web qui répertorie de nombreux mots clés, dans l'espoir d'augmenter son classement sur les moteurs de recherche. Un script sur la page redirige vers la page de l'attaquant.

^ 4, 1, 3, 2
^ Trojan = Cheval de Troie

---

![Course Notes Cybercrime_page-0027](https://user-images.githubusercontent.com/3305685/112466606-56f4da80-8d66-11eb-9d0c-982bc81bd234.jpg)

^ Nous venons d'étudier comment les logiciels malveillants peuvent être distribués et installés sur les ordinateurs des victimes. Ces ordinateurs infectés sont des précieuses ressources.

^ Ils ont une adresse IP unique, de la bande passante et des cycles CPU que l'on peut utiliser. De plus ils sont généralement bien réparti au travers d'Internet.

^ L'objectif de l'attaquant est de contrôler et d'utiliser ces machines, pour cela, il va transformer les machines infectés en un réseau de robots (botnet).

---

![Course Notes Cybercrime_page-0028](https://user-images.githubusercontent.com/3305685/112466609-578d7100-8d66-11eb-88d0-a56920b0eb9d.jpg)

^ Le bot master aura ensuite besoin d'une infrastructure pour contrôler les bots.

^ Il peut par exemple demander au robot de mettre à jour son malware ou envoyer des commandes aux robots pour qu'ils lancent des activités synchronisées.

^ Le réseau de robots peut être loué à d'autres malfaiteurs pour lancer leurs activités, comme l'envoi de spams.

^ Une fois en place, le botnet devient une plateforme permettant de lancer un grand nombre d'activités malveillantes et frauduleuses.

---

![Course Notes Cybercrime_page-0029](https://user-images.githubusercontent.com/3305685/112466613-58260780-8d66-11eb-8763-973487d12cd3.jpg)

^ La clé du succès d'un botnet réside dans un système de commande et de contrôle efficace et robuste. Ce n'est pas quelque chose de facile à mettre en place.

^ Par exemple un système contrôle centralisé tel que IRC permettrai de contrôler les bots à distances avec une simple commande.

^ Cependant, ce type de contrôle de commande n'est pas très robuste. Même s'il est très efficace, l'attaquant n'a qu'un seul canal de commande qui peut facilement être désactivé.

---

![Course Notes Cybercrime_page-0030](https://user-images.githubusercontent.com/3305685/112466617-59573480-8d66-11eb-81ef-8be6cae3bed5.jpg)

^ Une structure de contrôle de commande plus robuste consiste à utiliser un réseau P2P.

^ Ici, le botmaster peut se connecter à un certain nombre de bots dans ce réseau P2P pour envoyer ses commandes et mettre à jour le malware.

^ L'inconvénient est que le botmaster n'a pas une communication directe avec le botnet. Il ne pourra pas savoir combien de bots reçoivent ses commandes et quand.

---

![Course Notes Cybercrime_page-0031](https://user-images.githubusercontent.com/3305685/112466621-59efcb00-8d66-11eb-9658-d40863c4af45.jpg)

^ Aujourd'hui, l'approche la plus populaire pour le C&C est que tous les bots se connectent à un site web.

^ Le Botmaster peut rendre son système robuste en mappant le site web sur différentes adresses IP de façon à ce qu'il se déplace sur plusieurs serveurs.

---

![Course Notes Cybercrime_page-0032](https://user-images.githubusercontent.com/3305685/112466625-5b20f800-8d66-11eb-9c8a-22772405723e.jpg)

^ En fait, dans Fast Flux DNS, le Botmaster peut changer le mappage DNS IP du site web toutes les dix secondes.

^ Cela peut déjouer la détection ou le blocage, basés sur les adresses IP.

^ Mais comme le nom de domaine n'est pas modifié, ce domaine peut toujours être détecté comme étant utilisé pour le C&C du botnet.

^ Et les FAI peuvent bloquer l'accès à ce domaine.

---

![Course Notes Cybercrime_page-0033](https://user-images.githubusercontent.com/3305685/112466627-5bb98e80-8d66-11eb-97b1-66911c528554.jpg)

^ Au lieu d'utiliser des domaines fixes qui peuvent être détectés et bloqués. Les botmaster utilisent maintenant la génération de domaines aléatoires.

^ Chaque jour, un bot génère un grand nombre de noms de domaine au hasard.

^ Le botmaster dispose du même ensemble de domaines aléatoires, car les noms de domaines sont générés à l'aide du même algorithme et secret seed.

---

![Course Notes Cybercrime_page-0034](https://user-images.githubusercontent.com/3305685/112466633-5c522500-8d66-11eb-9b7c-abad8336859e.jpg)

^ Le botmaster n'enregistre que quelques-uns de ces domaines aléatoires. Bien que chaque bot génère de nombreux noms de domaines aléatoires, et les recherche tous, seuls quelques-uns d'entre eux se connecteront réellement aux sites web.

^ Cette approche de commande et de contrôle est très robuste, car elle est difficile à détecter. Les noms de domaines de C&C étant aléatoire, changent réguliérement et ils ne sont utilisés que pour période très courte.

---

# Penetration Testing

![](https://user-images.githubusercontent.com/3305685/112558587-68260180-8dcf-11eb-8690-dfdc91087084.jpeg)

^ Dans ce chapitre, nous allons aborder la première ligne de défense du réseau.

^ Les outils et techniques de base pour faire des tests de pénétration et évaluer la sécurité d'un réseau.

^ Nous aborderons également l'un des outils les plus puissants des hackers, vous.

^ L'ingénierie sociale est une méthode rapide et peu risquée pour accéder à des données.

---

![course_notes_PenetrationTesting_page-0001](https://user-images.githubusercontent.com/3305685/112641506-bfb18500-8e42-11eb-8dae-e8f57954a372.jpg)

^ Les tests de pénétration sont utilisés pour évaluer la sécurité d'un réseau. Cela comprend les procédures, opérations et technologies de votre organisation.

---

![course_notes_PenetrationTesting_page-0002](https://user-images.githubusercontent.com/3305685/112641508-c04a1b80-8e42-11eb-9126-4b4a39b82b6e.jpg)

^ Avec les tests de pénérations vous allez pouvoir déterminer si votre réseau est bien sécurisé et découvrir des vulnérabilités.

^ En exploitant ces vulnérabilités, vous allez pouvoir démontrer la probabilité que ces menaces se concrétisent et les dommages probables associés à ces menaces.

---

![course_notes_PenetrationTesting_page-0003](https://user-images.githubusercontent.com/3305685/112641510-c0e2b200-8e42-11eb-96b2-21f0624cefdb.jpg)

^ La portée des tests de pénétration ne se limite pas aux opérations techniques, elle peut également inclure l'ingénierie sociale et l'accès physique à votre organisation.

^ L'échelle du test inclut l'ensemble du réseau. Par exemple, le test peut inclure vos appareils mobiles, ou votre ordinateur portable.

---

![course_notes_PenetrationTesting_page-0004](https://user-images.githubusercontent.com/3305685/112641511-c0e2b200-8e42-11eb-906d-66c5abb93daf.jpg)

^ Les tests de pénétration comprennent plusieurs étapes:

^ 1. Trouver les informations générales de votre réseau.

^ 2. Trouver des informations plus détaillées sur votre réseau, comme les services qui y sont disponibles.

^ 3. Trouver des informations plus ciblées, comme le compte utilisateur.

^ 4. Trouve des vulnérabilités associées aux services du réseau, puis exploite ces vulnérabilités pour accéder au réseau.

^ 5. L'objectif est d'obtenir l'accès d'un super utilisateur.

^ 6. Le chapardage. Essayer de voler des informations sur le réseau.

^ 7. Le brouillage des pistes. Cacher les preuves de l'intrusion afin que les administrateurs de sécurité ne puissent pas facilement découvrir que le réseau a été attaqué.

^ 8. Création de portes dérobées. Créer un accès facile pour de futures activités malveillantes sur le réseau.

^ Les dernières étapes peuvent être répétées, par exemple pour passer d'un réseau à une autre.

---

![course_notes_PenetrationTesting_page-0005](https://user-images.githubusercontent.com/3305685/112641515-c17b4880-8e42-11eb-9049-128382f344e4.jpg)

^ Dans cette étape, l'attaquant, ou le testeur, effectue une reconnaissance et collecte des informations. Les informations réseau importantes comprennent les adresses IP du réseau, l'espace de noms et la topologie.

^ Ces informations sont essentielles pour planifier les prochaines étapes des tests ou des attaques. Par exemple, vous aurez besoin des adresses IP pour décider comment scanner le réseau.

---

![course_notes_PenetrationTesting_page-0006](https://user-images.githubusercontent.com/3305685/112641517-c17b4880-8e42-11eb-8c76-c0e931e431d1.jpg)

^ Nous allons énumérer ici les différentes techniques et les outils correspondants pour le footprinting.

^ Par exemple, vous pouvez utiliser Google pour trouver les informations sur l'entreprise, et utiliser Whois pour trouver les informations sur les noms de domaine des serveurs de noms et des plages IP.

---

![course_notes_PenetrationTesting_page-0007](https://user-images.githubusercontent.com/3305685/112641518-c213df00-8e42-11eb-9ee2-6e14d6b5bc78.jpg)

^ Une fois que vous avez obtenu les informations générales telles que les plages d'adresses IP d'un réseau, vous pouvez maintenant obtenir des informations plus détaillées sur le réseau en effectuant une analyse.

^ Vous pouvez savoir quelle machine est en marche et quels ports sont ouverts.

^ De même, sur les serveurs, quels sont les services en cours d'exécution.

^ Vous pouvez même découvrir les versions et les configurations de ces services pour ensuite rechercher les vulnérabilités correspondantes sur le Web.

^ Par exemple, pour une version particulière d'un serveur web Apache, vous pouvez rechercher si une vulnérabilité existe.

^ Les pistes les plus prometteuses sont généralement associées à services qui sont toujours en marche, comme les services web.

^ Vous voulez éviter de vous faire détecter, donc vous voulez donc réduire la fréquence et le volume de vos analyses.

---

![course_notes_PenetrationTesting_page-0008](https://user-images.githubusercontent.com/3305685/112641519-c213df00-8e42-11eb-9221-d74ba365997d.jpg)

^ Voici les différentes techniques et outils d'analyse.

^ Comme vous pouvez le voir, Nmap est l'un des outils les plus populaires. Il permet de découvrir quelles sont les machines sur un réseau, les ports ouverts et même déterminer le système d'exploitation.

---

![course_notes_PenetrationTesting_page-0009](https://user-images.githubusercontent.com/3305685/112641521-c2ac7580-8e42-11eb-8f8d-7a2d04664f8e.jpg)

^ Vous pouvez également effectuer des attaques ou des tests plus ciblés en déterminant quels sont les comptes d'utilisateurs mal protégés.

^ Ceci est plus ciblé et intrusif que le scan.

---

![course_notes_PenetrationTesting_page-0010](https://user-images.githubusercontent.com/3305685/112641522-c2ac7580-8e42-11eb-8f81-a59e64e34a13.jpg)

^ Par exemple, vous pouvez utiliser ces outils pour énumérer les comptes d'utilisateurs.

^ Et utiliser ces autres outils pour lister les services de partage de fichier.

---

![course_notes_PenetrationTesting_page-0011](https://user-images.githubusercontent.com/3305685/112641524-c3450c00-8e42-11eb-80cb-162bdcd3b8e3.jpg)

^ Une fois que vous avez obtenu les informations pertinentes sur les services réseau et les comptes d'utilisateur, vous pouvez maintenant exploiter et accéder au réseau.

^ En général, il existe des outils et scripts associés aux vulnérabilités connues que vous pouvez adapter à vos besoins.

^ En revanche, si la vulnérabilité est nouvelle ou s'il n'existe pas d'outil ou de script, vous devez développer vous-même l'exploit. En général, il s'agit d'un processus manuel qui peut être assez difficile.

---

![course_notes_PenetrationTesting_page-0012](https://user-images.githubusercontent.com/3305685/112641526-c3450c00-8e42-11eb-83bc-ceb78a157717.jpg)

^ Voici quelques exemples de techniques et d'outils permettant d'obtenir un accès.

^ Par exemple, vous pouvez utiliser des outils pour capturer et craquer un mot de passe. Il existe également des outils qui permettent d'exploiter les vulnérabilités de services les plus connus.

---

![course_notes_PenetrationTesting_page-0013](https://user-images.githubusercontent.com/3305685/112641527-c3450c00-8e42-11eb-875f-45eb5bcacb18.jpg)

^ L'étape suivante est l'escalade de privilège.

^ Le but est d'obtenir un accès de super utilisateur afin de pouvoir prendre le contrôle total du système.

---

![course_notes_PenetrationTesting_page-0014](https://user-images.githubusercontent.com/3305685/112641528-c3dda280-8e42-11eb-96f8-69386877e717.jpg)

^ Là encore, vous pouvez capturer et craquer les mots de passe des super utilisateurs.

^ Il existe des outils qui exploiteront les vulnérabilités des services ayant des privilèges afin de vous aider à obtenir un accès root.

---

![course_notes_PenetrationTesting_page-0015](https://user-images.githubusercontent.com/3305685/112641529-c3dda280-8e42-11eb-99c5-379f7c09fa82.jpg)

^ Une fois que vous obtenu l'accès au système. Vous allez pouvoir voler des informations précieuses. Ces informations peuvent vous permettre d'aller encore plus loin dans l'attaque.

---

![course_notes_PenetrationTesting_page-0016](https://user-images.githubusercontent.com/3305685/112641531-c4763900-8e42-11eb-9958-afa27a9305c7.jpg)

^ Par exemple, vous pourriez avoir accès à la base de données et récupérer les mot de passes non encryptés des utilisateurs.

---

![course_notes_PenetrationTesting_page-0017](https://user-images.githubusercontent.com/3305685/112641536-c4763900-8e42-11eb-90df-77711987ea2e.jpg)

^ Il est important de couvrir ses traces, afin que l'attaque ne puisse pas être détectée et arrêtée facilement.

---

![course_notes_PenetrationTesting_page-0018](https://user-images.githubusercontent.com/3305685/112641539-c50ecf80-8e42-11eb-9f88-0ed3232d508a.jpg)

^ Par exemple, vous pouvez utiliser ces outils pour modifier ou même effacer les journaux du système, et vous pouvez utiliser un rootkit pour cacher votre logiciel malveillant.

---

![course_notes_PenetrationTesting_page-0019](https://user-images.githubusercontent.com/3305685/112641541-c50ecf80-8e42-11eb-9aee-425c5104e305.jpg)

^ La première fois que l'on accède à un réseau par le biais d'un exploit est toujours difficile.

^ Et comme vous voulez que l'accès ultérieur soit facile et paraisse normal, vous allez créer des portes dérobées.

---

![course_notes_PenetrationTesting_page-0020](https://user-images.githubusercontent.com/3305685/112641542-c5a76600-8e42-11eb-81d8-266d92d15f09.jpg)

^ Il existe de nombreuses techniques et outils.

^ Par exemple, vous pouvez créer de faux comptes d'utilisateur ou ajouter des services d'accès à distance.

^ Vous pouvez également programmer vos activités à une certaine heures.

---

# Penetration Testing Quiz

Quels événements doivent déclencher un test de pénétration ?

- [ ] Une infrastructure est ajoutée ou modifiée
- [ ] Des applications sont ajoutées ou modifiées
- [ ] Changement de la politique d'utilisation de l'utilisateur final
- [ ] Installation de correctifs de sécurité

^ Tous ces événements devraient déclencher un test de pénétration. Les tests de pénérations doivent également être effectués sur de manière régulière.

---

# Hacking Workshop

[https://github.com/melkir/hacking-workshop](https://github.com/melkir/hacking-workshop)

---

![fb-what-is-https](https://user-images.githubusercontent.com/3305685/113394136-ff72f200-9397-11eb-8dab-c34b1cb0a379.png)

^ Discutons du HTTPS et de la manière dont il est intégré au navigateur Web.

---

# Qu'est-ce que HTTPS ?

Le protocole de transfert hypertexte sécurisé (HTTPS) est la version sécurisée de HTTP.

Il s'agit du protocole principal utilisé pour envoyer des données entre un navigateur web et un site web.

<sub>Source: [Cloudflare - What is HTTPS?](https://www.cloudflare.com/fr-fr/learning/ssl/what-is-https/)</sub>

---

# Qu'est-ce que HTTPS ?

Le traffic HTTPS est chiffré afin d'augmenter la sécurité du transfert de données. Ce chiffrement est particulièrement important lorsque les utilisateurs transmettent des données sensibles.

- Connexion à un compte bancaire
- Connexion à un service de messagerie électronique
- Connexion à une compagnie d'assurance maladie.

^ Tous les sites web, en particulier ceux qui nécessitent des informations de connexion, doivent utiliser HTTPS.

---

# Qu'est-ce que HTTPS ?

Ce type de système de sécurité utilise deux clés différentes pour chiffer les communications entre deux parties :

- La clé privée - cette clé est contrôlée par le propriétaire d'un site web et maintenue privée. Cette clé réside sur un serveur web. Elle est utilisée pour déchiffrer les informations chiffrées par la clé publique.

- La clé publique - cette clé est disponible pour tous ceux qui souhaitent interagir avec le serveur de manière sécurisée. Les informations chiffrées par la clé publique ne peuvent être déchiffrées que par la clé privée.

^ Les données sont chiffrées grâce à la cryptographie asymétrique et ainsi envoyées de manière sécurisée.

---

![4  Course Notes Advanced Web SecurityP3_page-0003](https://user-images.githubusercontent.com/3305685/113414866-4542b100-93be-11eb-826a-c3cfed8b791f.jpg)

^ Les communications qui ont lieu en HTTP se font en texte brut, elles sont donc accessibles à toute personne disposant des outils appropriés (Man-In-The-Middle).

^ Une personne ayant accès au même réseau Wi-Fi (ex: Wi-Fi public), sera capable de "renifler" les paquets qui transitent sur le réseau avec un outil tel que WireShark.

---

# Wireshark: Attaque de l'homme du milieu

![inline](https://user-images.githubusercontent.com/3305685/113408701-21786e80-93b0-11eb-8ef2-5f75ae04cd2f.jpg)

---

![4  Course Notes Advanced Web SecurityP3_page-0004](https://user-images.githubusercontent.com/3305685/113414868-45db4780-93be-11eb-9750-976330da916d.jpg)

---

# Pourquoi le HTTPS est-il important ?

[.column]

HTTPS élimine également la possibilité pour des tiers non modérés, d'injecter du contenu sur une page web.

Par exemple, sans chiffrement, il est possible pour un FAI d'injecter une publicité dans une pages web sans l'approbation du propriétaire du site.

[.column]

![inline](https://www.cloudflare.com/img/learning/security/glossary/what-is-https/third-party-content.png)

^ Les bénéfices issus des annonces publicitaires et le contrôle qualité de ces annonces ne sont en aucun cas partagés avec le propriétaire du site.

---

![inline](https://user-images.githubusercontent.com/3305685/113395011-84124000-9399-11eb-93d3-be6fdb1b8567.png)

^ Mars 2021 | France: 94% des pages sont chargées via HTTPS

^ https://transparencyreport.google.com/https/overview

---

# HTTPS Quiz

Quels sont les éléments qui peuvent être chiffrées par HTTPS ?

- [ ] URL de la requête
- [ ] Paramètres de la requête
- [ ] En-têtes
- [ ] Cookies
- [ ] Adresses des hôtes
- [ ] Numéros de port
- [ ] La quantité de données transférées
- [ ] La durée de la session

^ Vrai, Vrai, Vrai, Vrai

^ Les adresses et n° de port sont utilisées pour diriger le trafic.

^ La quantité de données transférées et la durée de la session peuvent être déterminées en observant le trafic.

---

# En quoi HTTPS est-il différent de HTTP ?

Techniquement parlant, HTTPS n'est pas un protocole distinct de HTTP. Il utilise simplement le **chiffrement** TLS/SSL sur le protocole HTTP.

HTTPS repose sur la transmission de **certificats** TLS/SSL, qui vérifient qu'un fournisseur particulier est bien celui qu'il prétend être.

^ Lorsqu'un utilisateur se connecte à une page web, la page web envoie son certificat SSL qui contient la clé publique nécessaire pour démarrer la session sécurisée.

---

# Comment fonctionne le SSL/TLS ?

- Afin de garantir un degré élevé de **confidentialité**, le SSL chiffre les données transmises sur le Web. Cela signifie que quiconque tente d'intercepter ces données ne verra qu'un mélange confus de caractères quasiment impossible à déchiffrer.

- Le SSL lance un processus d'**authentification** appelé handshake entre deux dispositifs de communication pour s'assurer que les deux appareils sont vraiment ceux qu'ils prétendent être.

- Le SSL signe également numériquement les données afin d'assurer l'**intégrité** des données, en vérifiant que les données ne sont pas falsifiées avant d'atteindre leur destinataire prévu.

^ **La non-répudiation**: Aucun tiers ne doit pouvoir s'attribuer les actions d'un autre utilisateur.

---

# Comment un site web commence-t-il à utiliser HTTPS ?

De nombreux hébergeurs de sites web et d'autres services proposent des certificats TLS/SSL contre rémunération. Ces certificats seront souvent partagés entre de nombreux clients.

Des certificats plus chers sont disponibles et peuvent être enregistrés individuellement sur des propriétés web particulières.

---

# Cryptographie asymétrique

[.column]

![inline](https://user-images.githubusercontent.com/3305685/113476730-95cd1380-947d-11eb-8772-cf5ceee6baa4.png)

[.column]

![inline](https://user-images.githubusercontent.com/3305685/113476732-96fe4080-947d-11eb-808e-b8de8066a6fb.png)

^ 1: Alice génère deux clefs. La clef publique (verte) qu'elle envoie à Bob et la clef privée (rouge) qu'elle conserve précieusement sans la divulguer à quiconque.

^ 2: Bob chiffre le message avec la clef publique d'Alice et envoie le texte chiffré.

^ 3: Alice déchiffre le message grâce à sa clef privée.

---

![4  Course Notes Advanced Web SecurityP3_page-0010](https://user-images.githubusercontent.com/3305685/113414879-483da180-93be-11eb-9649-97aaab6fbe66.jpg)

^ Un problème essentiel de la cryptographie asymétrique est de savoir comment Alice peut obtenir la clé publique de Bob.

^ La norme est d'utiliser un certificat émis par une autorité de certification, que nous appelons l'AC.

^ Tout d'abord, chaque entité doit installer la clé publique du l'AC.

^ Ensuite, Bob peut demander à l'autorité de certification de générer un certificat pour sa clé publique.

^ L'autorité de certification garde pour elle la clé privée de signature.

^ L'autorité de certification signe la clé publique de Bob à l'aide de sa clé privée de signature et la signature est intégrée au certificat.

^ Bob peut donc maintenant présenter le certificat à Alice.

^ Et comme Alice a la clé publique de l'autorité de certification, elle peut vérifier que la signature a été construite correctement.

^ Ce qui signifie que la clé publique de Bob a été certifiée par l'autorité de certification.

---

![4  Course Notes Advanced Web SecurityP3_page-0011](https://user-images.githubusercontent.com/3305685/113414880-483da180-93be-11eb-9ab0-0000bc587891.jpg)

^ Voici un exemple de certificat de clé publique. Passons en revue quelques informations importantes.

^ Premièrement, il y a un numéro de série unique.

^ Deuxièmement, il y a une période de validité.

^ Enfin, il y a une clé publique et une signature produites par l'autorité de certification.

---

![4  Course Notes Advanced Web SecurityP3_page-0012](https://user-images.githubusercontent.com/3305685/113414881-48d63800-93be-11eb-81a3-fc6042a8a73d.jpg)

^ Voici un exemple d'informations de certificat qu'un utilisateur voit sur son ordinateur.

^ Il indique que le certificat concerne la clé publique de mail.google.com.

---

![4  Course Notes Advanced Web SecurityP3_page-0013](https://user-images.githubusercontent.com/3305685/113414883-48d63800-93be-11eb-8c7d-f48a443498b6.jpg)

^ Un certificat est destiné à une entité ou à un sujet identifié par le nom commun.

^ Qu'est-ce qu'un nom commun ? Un nom commun peut être un nom explicite, par exemple cc.gatech.edu.

^ Il peut aussi être un wildcard, par exemple \*.gatech.edu.

^ Si un caractère générique est utilisé, il ne peut être que le composant le plus à gauche, et il ne correspond pas au point.

^ Par exemple : \*.a.com correspond à x.a.com mais pas à y.x.a.com.

---

![4  Course Notes Advanced Web SecurityP3_page-0014](https://user-images.githubusercontent.com/3305685/113414885-496ece80-93be-11eb-9c18-96054a2f8498.jpg)

^ Il existe un grand nombre d'autorités de certification, et un navigateur accepte généralement les certificats de 60 autorités de certification de premier niveau et de 1200 autorités de certification intermédiaires.

---

![4  Course Notes Advanced Web SecurityP3_page-0015](https://user-images.githubusercontent.com/3305685/113414886-4a076500-93be-11eb-8eac-f7ff84821b62.jpg)

^ Le but de la poignée de main est d'authentifier le serveur et, de manière optimale, le navigateur.

^ Plus important encore, à la fin, les deux entités auront une clé secrète partagée qui pourra être utilisée pour chiffrer le trafic HTTP.

^ Le client envoie un message hello au serveur et la réponse du serveur comprend un certificat de clé publique.

^ Le navigateur vérifie le certificat auprès de l'AC, afin d'authentifié le serveur avec sa clé publique.

^ Avec la PK d'un serveur, le navigateur et le serveur effectue un échange de clés sécurisé (Diffie-Hellman) afin d'éviter les attaques de type "man-in-the-middle".

^ Le résultat est qu'ils ont établis une clé secrète partagée et qu'ils peuvent maintenant utiliser cette clé secrète partagée pour chiffrer les données HTTP.

---

![4  Course Notes Advanced Web SecurityP3_page-0016](https://user-images.githubusercontent.com/3305685/113414888-4a076500-93be-11eb-877f-7e0eb22b8424.jpg)

^ HTTPS est indiqué dans l'interface graphique du navigateur.

^ L'objectif est de permettre à l'utilisateur de savoir d'où vient une page.

^ Il indique également aux utilisateurs que le contenu de la page est protégé, càd qu'un attaquant du réseau ne pourra pas voir ou modifier la page.

^ En réalité, il existe plusieurs problèmes de sécurité.

---

![4  Course Notes Advanced Web SecurityP3_page-0017](https://user-images.githubusercontent.com/3305685/113414891-4a9ffb80-93be-11eb-8069-e29b6645bb05.jpg)

^ Lorsque l'icône de verrouillage est affichée sur le navigateur, cela signifie que tous les éléments de la page sont récupérés en utilisant HTTPS.

^ Mais pour que le navigateur accepte cette connexion HTTPS, cela signifie que le navigateur a fait confiance au certificat et vérifié que le certificat est valide.

^ De plus, l'URL du domaine correspond au CommonName ou au SubjectAlternativeName du certificat.

---

![4  Course Notes Advanced Web SecurityP3_page-0018](https://user-images.githubusercontent.com/3305685/113414892-4b389200-93be-11eb-971a-189e70c7a0a3.jpg)

^ Par exemple, le certificat de google.com peut simplement fournir une liste de noms alternatifs.

---

# HTTPS Disadvantages Quiz

- [ ] La mise en cache du navigateur ne fonctionne pas correctement.
- [ ] Vous devez acheter un certificat SSL
- [ ] HTTPS utilise beaucoup de ressources serveur
- [ ] Problèmes de mise en cache par proxy - la mise en cache publique ne peut pas avoir lieu.
- [ ] HTTPS introduit des latences notables

^ Faux

^ Vrai

^ Faux

^ Vrai

^ Faux

---

![4  Course Notes Advanced Web SecurityP3_page-0020](https://user-images.githubusercontent.com/3305685/113414895-4bd12880-93be-11eb-8a0a-7de4441d943b.jpg)

^ Discutons de plusieurs problèmes de sécurité avec HTTPS et l'icône de verrouillage.

^ Cela inclut le passage de HTTP à HTTPS.

^ Les faux certificats.

^ Tout d'abord, discutons de la mise à niveau de HTTP à HTTPS.

^ Il existe une méthode d'attaque appelée "SSL stripped".

^ Elle empêche le navigateur d'effectuer la mise à niveau de HTTP vers HTTPS.

---

![4  Course Notes Advanced Web SecurityP3_page-0021](https://user-images.githubusercontent.com/3305685/113414897-4bd12880-93be-11eb-87fc-81f41f35a2af.jpg)

^ Avec la suppression de SSL, le navigateur n'affiche aucune erreur de certificat SSL et l'utilisateur n'a aucune idée de l'existence d'une telle attaque.

^ Cette attaque est également connue sous le nom d'attaque "HTTP downgrading".

^ La connexion établie entre le navigateur de l'utilisateur victime et le serveur web est déclassée de HTTPS à HTTP.

^ La connexion entre l'attaquant et la banque est sécurisée tandis que la connexion entre l'attaquant et le client est non sécurisée.

^ Pour cela l'attaquant a accès à la page de connexion et peut modifier la réponse du serveur de HTTPS en HTTP, puis transmettre la page de connexion en HTTP au client.

^ À partir de ce moment, toutes les requêtes de l'utilisateur sont envoyées en clair, et l'attaquant peut accéder aux données et collecter les informations d'identification.

^ Alors que le serveur pense avoir utilisé une connexion sécurisée, cette connexion n'est en fait qu'entre le serveur web de la banque et l'attaquant.

^ D'autre part, le navigateur de l'utilisateur utilise la connexion HTTP non sécurisée, pensant que c'est ce que le serveur web de la banque veut qu'il utilise.

---

![4  Course Notes Advanced Web SecurityP3_page-0022](https://user-images.githubusercontent.com/3305685/113414898-4c69bf00-93be-11eb-9592-8e217cd4fa2d.jpg)

^ La solution à l'attaque "SSL stripped" est d'utiliser HSTS, qui signifie Strict Transport Security.

^ Elle indique au navigateur web de toujours utiliser HTTPS, même pour pour les sous-domaines.

^ Il existe également une extension sur Chrome nommé HTTPS Everywhere.

---

![4  Course Notes Advanced Web SecurityP3_page-0023](https://user-images.githubusercontent.com/3305685/113414899-4c69bf00-93be-11eb-8ad3-754ebdf8afe7.jpg)

^ Lorsqu'un navigateur Web visite un site Web pour la première fois, le site Web peut indiquer au navigateur de toujours utiliser le protocole HTTPS.

^ En d'autres termes, pour toute visite ultérieure, toutes les connexions doivent se faire en HTTPS, et les connexions HTTP seront rejetées.

^ Un navigateur web peut également avoir une liste préchargée de sites web HSTS.

^ Avant même que le navigateur web ne visite un site figurant sur cette liste, il sait qu'il doit utiliser HTTPS.

^ Le drapeau HSTS, activé par un site web peut être effacé lorsque l'utilisateur sélectionne "Effacer les données privées".

---

![4  Course Notes Advanced Web SecurityP3_page-0024](https://user-images.githubusercontent.com/3305685/113414900-4d025580-93be-11eb-9c59-bd2e5e07cc78.jpg)

^ Les certificats falsifiés constituent un autre problème de sécurité grave.

^ Par exemple, si une autorité de certification est piratée, l'attaquant peut émettre des certificats falsifiés.

^ Par exemple, pour Gmail, une fois qu'un certificat falsifié est émis, l'attaquant peut créer un faux site Web et s'appeler Gmail.

^ Plusieurs pays ont été surpris à émettre des certificats non autorisés, par exemple pour Google, afin que les FAI de ces pays puissent jouer les intermédiaires entre un utilisateur et le véritable serveur Google.

---

![4  Course Notes Advanced Web SecurityP3_page-0025](https://user-images.githubusercontent.com/3305685/113414902-4d025580-93be-11eb-93d6-b852628383f4.jpg)

^ L'exemple suivant illustre bien ce phénomène.

^ Supposons qu'un utilisateur veuille se connecter à une banque.

^ Il y a un attaquant au milieu avec un faux certificat, il se fait donc passer pour la banque.

^ L'utilisateur peut penser qu'il est connecté à la banque puisque le certificat le dit.

^ Cependant le certificat étant faux, l'utilisateur est en fait connecté au méchant.

^ Cela montre qu'avec un certificat douteux, un attaquant peut jouer à l'homme du milieu, même dans une connexion HTTPS.

^ L'attaquant joue le rôle du serveur de la banque pour l'utilisateur et de l'utilisateur pour le serveur de la banque.

^ Et les deux côtés des connexions sont en HTTPS.

---

![4  Course Notes Advanced Web SecurityP3_page-0026](https://user-images.githubusercontent.com/3305685/113414903-4d025580-93be-11eb-826b-75657bf8e174.jpg)

^ Une approche pour traiter les certificats falsifiés consiste à utiliser l'épinglage dynamique des clés publiques.

^ Cela signifie qu'un site Web déclare les AC qui peuvent signer son certificat.

^ Lorsqu'un navigateur visite un site Web pour la première fois, ce dernier lui indique la liste des autorités de certification autorisées.

^ Ensuite, lors des visites suivantes, le navigateur rejettera tout certificat émis par d'autres AC.

---

![4  Course Notes Advanced Web SecurityP3_page-0027](https://user-images.githubusercontent.com/3305685/113414904-4d9aec00-93be-11eb-8e62-92e9bad94f5e.jpg)

^ De manière très similaire, il existe une extension d'épinglage de clé publique pour HTTP ou HPKP.

^ Cette fonctionnalité indique à un navigateur web la liste des clés appropriées à associer au site web.

^ Et elle peut empêcher les attaques de type "man-in-the-middle" avec de faux certificats.

^ Lorsque le navigateur visite un site Web pour la première fois, il envoie une liste de hachages de clés publiques.

^ Lors des visites suivantes, le navigateur s'attend à ce que le serveur utilise une ou plusieurs de ces clés publiques dans ses certificats.

---

![4  Course Notes Advanced Web SecurityP3_page-0028](https://user-images.githubusercontent.com/3305685/113414905-4d9aec00-93be-11eb-808f-4938707f80e1.jpg)

^ Un autre problème lié à la falsification des certificats consiste à rendre les autorités de certification transparentes.

^ En d'autres termes, les AC doivent publier dans un registre public tous les certificats qu'elles ont émis et un navigateur n'acceptera un certificat que s'il est publié dans un registre public.

^ Des entreprises comme Google peuvent constamment scanner les journaux publics afin de rechercher des certificats invalides ou falsifiés.

---

# Ressources

- [udacity.com > Network Security UD199](https://www.udacity.com/course/network-security--ud199)

- [udemy.com > Complete Ethical Hacking Bootcamp](https://www.udemy.com/course/complete-ethical-hacking-bootcamp-zero-to-mastery/)

- [cs.cornell.edu > Taxonomy CCR](http://www.cs.cornell.edu/courses/cs619/2004fa/documents/taxonomy-ccr.pdf)

- [napsis.fr > Réseau Modele OSI](https://www.napsis.fr/actualite/reseau-modele-osi/)

- [cloudflare.com > What is HTTPS?](https://www.cloudflare.com/fr-fr/learning/ssl/what-is-https/)

- [cloudflare.com > DNS Amplification DDOS Attack](https://www.cloudflare.com/fr-fr/learning/ddos/dns-amplification-ddos-attack/)

- [transparencyreport.google.com > HTTPS Overview](https://transparencyreport.google.com/https/overview)

- [fr.wikipedia.org > Cryptographie Asymétrique](https://fr.wikipedia.org/wiki/Cryptographie_asym%C3%A9trique)

- [cert-ist.com > Syn Cookies](https://www.cert-ist.com/public/fr/SO_detail?code=Syn_Cookies)
