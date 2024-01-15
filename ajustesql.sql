BEGIN;
--
-- Add field agencia to graduacao
--
ALTER TABLE "aluno_graduacao" ADD COLUMN "agencia" varchar(200) NULL;
--
-- Add field bolsa_graduacao to graduacao
--
ALTER TABLE "aluno_graduacao" ADD COLUMN "bolsa_graduacao" boolean DEFAULT false NOT NULL;
ALTER TABLE "aluno_graduacao" ALTER COLUMN "bolsa_graduacao" DROP DEFAULT;
--
-- Add field iniciacao_cientifica to graduacao
--
ALTER TABLE "aluno_graduacao" ADD COLUMN "iniciacao_cientifica" boolean DEFAULT false NOT NULL;
ALTER TABLE "aluno_graduacao" ALTER COLUMN "iniciacao_cientifica" DROP DEFAULT;
COMMIT;
