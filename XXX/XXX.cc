//
// ---------- header ----------------------------------------------------------
//
// project       XXX.cc
//
// license       infinit
//
// author           [thu sep 22 08:57:11 2011]
//

#include <Infinit.hh>
#include <elle/Elle.hh>
#include <etoile/Etoile.hh>
#include <nucleus/Nucleus.hh>
#include <lune/Lune.hh>
#include <hole/Hole.hh>

#include <XXX/Porcupine.hh>

int main(int argc, char** argv)
{
  // allocate a new parser.
  Infinit::Parser = new elle::Parser(argc, argv);

  elle::Elle::Initialize();
  nucleus::Nucleus::Initialize();
  lune::Lune::Initialize();
  Infinit::Initialize();

  Infinit::Parser->Parse();

  // XXX
  Infinit::Network = "kapoue";
  hole::Hole::Initialize();

  expose();

  // XXX
  nucleus::Porcupine<>::Initialize(
    elle::Callback<>::Infer(&etoile::Nest::Attach),
    elle::Callback<>::Infer(&etoile::Nest::Detach),
    elle::Callback<>::Infer(&etoile::Nest::Load),
    elle::Callback<>::Infer(&etoile::Nest::Unload));

  nucleus::Porcupine<nucleus::Catalog>* p =
    new nucleus::Porcupine<nucleus::Catalog>;

  const int n = 50000;

  std::vector<elle::String> v(n);

  for (int i = 0; i < n; i++)
    {
      elle::String s;

      elle::Random::Generate(s, 16);

      v[i] = s;
    }

  /* XXX
  for (int i = 0; i < n; i++)
    {
      char buffer[128];

      sprintf(buffer, "%d", i);

      elle::Digest digest;

      elle::OneWay::Hash(elle::Region((elle::Byte*)buffer, strlen(buffer)),
                         digest);

      elle::String s;

      elle::Hexadecimal::Encode(digest.region, s);

      v[i] = s.substr(0, 16);
    }
  */

  for (int i = 0; i < n; i++)
    {
      printf("[%u] -------------> %s\n", i, v[i].c_str());

      Handle value;

      if (nucleus::Porcupine<>::Attach.Call(new nucleus::Catalog,
                                            value) == elle::StatusError)
        fail("unable to attach the value");

      if (p->Add(v[i], value) == elle::StatusError)
        fail("XXX");
    }

  if (p->Check() == elle::StatusError)
    fail("XXX");

  //p->Dump();

  for (int i = 0; i < n; i++)
    {
      nucleus::Handle   h;

      printf("[%u] -------------= %s\n", i, v[i].c_str());

      if (p->Locate(v[i], h) == elle::StatusError)
        fail("XXX");

      if (nucleus::Porcupine<>::Detach.Call(h) == elle::StatusError)
        fail("unable to detach the value");
    }

  if (p->Check() == elle::StatusError)
    fail("XXX");

  //p->Dump();

  for (int i = 0; i < n; i++)
    {
      printf("[%u] -------------< %s\n", i, v[i].c_str());

      if (p->Remove(v[i]) == elle::StatusError)
        fail("XXX");

      //if (p->Check() == elle::StatusError)
      //fail("XXX");
    }

  if (p->Check() == elle::StatusError)
    fail("XXX");

  p->Dump();

  etoile::Nest::Show();

  delete p;

  expose();

  delete Infinit::Parser;

  hole::Hole::Clean();
  Infinit::Clean();
  lune::Lune::Clean();
  nucleus::Nucleus::Clean();
  elle::Elle::Clean();

  return 0;
}
